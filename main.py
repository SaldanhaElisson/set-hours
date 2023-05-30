from formula import Atom
from pysat.formula import IDPool
from pysat.solvers import Cadical153

var_pool = IDPool()
solver = Cadical153()

coursesSmall = ["HTML", "PHP", "MySQL", "Swift"]
slots: int = 3
conflicts = [[1, 2], [2, 3], [2,4], [3, 4]]


allForm = []

# Cursos tem de estar em no mínimo UM horário
def atLeastOneSlot():
  for c in range(0, len(coursesSmall)):
      firstForm = []
      for s in range(0, slots):
          firstForm.append(var_pool.id(Atom("X_{}_{}".format(c+1, s+1))))
      allForm.append(firstForm)

   
atLeastOneSlot()

# Cursos só podem ser ofertados em no Máximo UM horário

def onlyOneSlot():
  for c in range(0, len(coursesSmall)):
      for s in range(0, slots):
        for n in range(s+1, slots):
          secondForm = []
          secondForm.append(-1*var_pool.id(Atom("X_{}_{}".format(c+1, s+1))))
          secondForm.append(-1*var_pool.id(Atom("X_{}_{}".format(c+1, n+1))))
          allForm.append(secondForm)

onlyOneSlot()

# (~X1,1 v ~X2,1) ^....^(~X1,s v...v ~Xc,s)
# Cursos em Conflito não podem ter o mesmo horário
def noConflicts():
    for z in range(0, len(coursesSmall)):
      for j in range(0, len(coursesSmall)):
          if [z+1,j+1]  in conflicts:
            for s in range (0, slots): 
                  thirdForm = []
                  thirdForm.append(-1*var_pool.id(Atom("X_{}_{}".format(z+1, s+1))))
                  thirdForm.append(-1*var_pool.id(Atom("X_{}_{}".format(j+1, s+1))))
                  allForm.append(thirdForm)

noConflicts()



## colocar na tela todas as formulas
for x in allForm:
    print(x)