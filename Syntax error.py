#Syntax error
#An error that occurs when one violets the rules and standards in pythone
#Eg
"""print("hello World"
      
#IndentationError
if (number <20):
print("Less than 20")

#Run time errors
#Errors where the code is written perfectly but error comes during running
x = 10
y = 0
divid = x/y

a = [1,2,3]
print(a[4])"""


#TRY AND CATCH BLOCK TO HANDLE RUN TIME ERRORS

interator = True
x = 0
y = 0

#Runtime Error
while interator:
    try:
       if x <= 0:
           x = int(input("Enter number: "))
       if y <= 0:
          y = int(input("Enter: "))
       
          divide = x/y
          
          interator = False
    except ZeroDivisionError:
       ("Please don't divide by zero")  
       
#Catching value error
    except ValueError:
     print("Please only enter numeric values")

print("EDUBE EMMA")



