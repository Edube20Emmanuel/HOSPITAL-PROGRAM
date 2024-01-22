
interator = 0


while interator in range(5): 
   try:
         
      numer_one= int(input("Enter first number: "))
      nuumber_two= int(input("Enter second number: "))
         
      while True:
         operator = input("Enter operator,(*,+,-,/): ")
         if operator in ("*","+","-","/"):
               break
         else:
            print("Invalid entry, please choose from available options: ")
            

      division = numer_one/nuumber_two 
      multiplication =numer_one*nuumber_two
      subtraction =numer_one-nuumber_two
      addition = numer_one + nuumber_two   

      Result =int(input("Enter answer: "))

      if operator == "/" and Result == division:
         print("Correct")
         interator = interator +1
         break
      elif operator == "+" and Result == addition:
         print("correct")
         interator = interator +1
         
      elif operator =="-" and Result == subtraction:
         print("Correct")
         interator = interator +1
      elif operator == "*" and Result == multiplication:
         print("Correct")
         interator = interator +1

      else:
         print("Wrong!")

       
             
             
   except ZeroDivisionError:
      ("Please don't divide by zero")  
       
#Catching value error
   except ValueError:
      
      print("Please only enter numeric values")

   print("Enjoy mathematics")
