from formula import Atom
from pysat.formula import IDPool
from pysat.solvers import Minisat22

coursesSmall = []
conflicts = []


def getInputData():
    qtdCourses = int(input("Digite a quantidade de MiniCursos: "))
    courseNumber: int = 0;

    while (courseNumber < qtdCourses):
        courseName = str(input("Digite o nome do curso {} ".format(courseNumber + 1)))
        coursesSmall.append(courseName)
        courseNumber = courseNumber + 1

    qtdConflicts = int(input("Digite a quantidade de conflitos: "))
    print("Para colocar as incrições digite os pares de cursos com uma espaço entre eles, exemplo 1 2")
    clonflictsNumber: int = 0;
    while (clonflictsNumber < qtdConflicts):
        conflictInput = str(input("Digite o conflito: "))
        conflict = conflictInput.split(" ")
        conflicts.append([int(val) for val in conflict])
        clonflictsNumber = clonflictsNumber + 1


getInputData()

slots = int(input("Digite a quantidade de slots: "))

var_pool = IDPool()
solver = Minisat22()

allForm = []


# (~X1,1 v ~X2,1) ^....^(~X1,s v...v ~Xc,s)

def atLeastOneSlot():
    for c in range(0, len(coursesSmall)):
        firstForm = []
        for s in range(0, slots):
            firstForm.append(var_pool.id(Atom("X_{}_{}".format(c + 1, s + 1))))
        allForm.append(firstForm)


atLeastOneSlot()


# (x1,1 v X1,2 v X1,3 v .... v X1,s) ^ ..... ^ (Xc, 1 v Xc,2 v Xc,3 ... Xc,s)

def onlyOneSlot():
    for c in range(0, len(coursesSmall)):
        for s in range(0, slots):
            for n in range(s + 1, slots):
                secondForm = []
                secondForm.append(-1 * var_pool.id(Atom("X_{}_{}".format(c + 1, s + 1))))
                secondForm.append(-1 * var_pool.id(Atom("X_{}_{}".format(c + 1, n + 1))))
                allForm.append(secondForm)


onlyOneSlot()


# (~X1,1 v ~X2,1) ^....^(~X1,s v...v ~Xc,s)

def noConflicts():
    # Compara se o index z e j da lista de cursos possui conflito (+1 é adicionado para comparar com os recebidos na lista de conflitos)
    for z in range(0, len(coursesSmall)):
        for j in range(0, len(coursesSmall)):
            if [z + 1, j + 1] in conflicts:
                for s in range(0, slots):
                    thirdForm = []
                    thirdForm.append(-1 * var_pool.id(Atom("X_{}_{}".format(z + 1, s + 1))))
                    thirdForm.append(-1 * var_pool.id(Atom("X_{}_{}".format(j + 1, s + 1))))
                    allForm.append(thirdForm)


noConflicts()

## colocar na tela todas as formulas que estão da lista maior (and)
# for x in allForm:
#     print(x)

solver.append_formula(allForm)
isSolver = solver.solve()
courseSlots = []


def formatResult():
    atomicas = solver.get_model()

    for n in atomicas:
        if (n < 0):
            continue
        courseSlots.append(var_pool.obj(n).__str__().split("_"))


def printResult():
    print("Saídas: ")
    # Printa na forma Xcurso,slot com valor verdadeiro para o resultado e depois dá as sáidas do print anterior indicando o número do curso e o slot que ele vai ser ofertado
    if (isSolver):
        formatResult()
        for [_, course, slot] in courseSlots:
            print("{} s{}".format(course, slot))
    else:
        print("Não é possível alocar slots para os cursos")


printResult()
