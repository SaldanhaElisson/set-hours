from formula import Atom

coursesSmall = ["HTML", "PHP", "MySQL", "Swift"]
slots: int = 3
conflicts = [[1, 2], [2, 3], [2,4], [3, 4]]



def atLeastOneSlot():
    allForm = []
    for c in range(0, len(coursesSmall)):
        firstForm = []
        for s in range(0, slots):
            firstForm.append(Atom("X_{}_{}".format(c+1, s+1)))
        allForm.append(firstForm)

    for x in allForm:
        for p in x:
            print(p.__str__())
        print(" ")


makeOnlyOne()
