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
          Result = divide
          interator = False
    except ZeroDivisionError:
       ("Please don't divide by zero")  
       