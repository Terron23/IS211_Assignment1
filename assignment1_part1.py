


def listDivide(numbers, divide=2):
    count = 0
    for i in numbers:
        if(i%divide ==0):
            count +=1
    return count
    

class ListDivideException:
    def __init__(self):
        print("Invalid! Try again.")

def testListDivide():
    if listDivide([1,2,3,4,5]) != 2 or listDivide([2,4,6,8,10]) != 5 or listDivide([30, 54, 63,98, 100], 10) != 2 or listDivide([]) != 0 or listDivide([1,2,3,4,5], 1) != 5 :
        ListDivideException()

testListDivide()
