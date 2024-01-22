print("ENTER YOUR NAME")
userName =input()
print("HELLO",userName)

#DEFINE FUNCTION
def greet(name):
    print("Good afternoon",name)
greet("EDUBE")
greet("ANITA")
greet("JOY")

#WHEN U ASK THE USER TO ENTER NAME
fN =input("Enter your full name:")
greet(fN)

#PRACTICE
def revenue():
    tution = 2.5
    grant = 0.5
    don = 0.2
    proj = 3.0
    total =  tution+grant+don+proj
    print("Total revenue is:",total)
revenue()

#specifying arguments
def rev(tut:float,gr:float,do:float,pj:float) -> float:
   tr = tut + gr + do + pj
   return tr
print(rev(6.0,4.2,7.3,3.0))
print(rev(4.5,2.2,7.3,3.0))
totrev = rev(6.0,4.2,7.3,3.0)
print(totrev)
