#GREETING
def gr(fname):
    print("How are you today!",fname)

#COMPUTE COURSE WORK
def cw(t1:int,t2:int,t3:int) ->int:
    cwmrk =(t1 + t2 + t3)/3
    return cwmrk

#COMPUTE EXAM
def ex(pr:int,th:int) ->int:
    exmrk =pr + th
    return exmrk

print ("Welcome to the resuls app")
stName = input("Please enter name")
gr(stName)
test1= int(input("Enter score for test 1:"))
test2 = int(input("Enter score for test 2:"))
test3 = int(input("Enter score for test 3:"))
cw(test1,test2,test3)
coursework =test1 + test2 + test3
print(coursework)
