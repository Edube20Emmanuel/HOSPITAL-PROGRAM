#LOOPS LESSON
#WHILE LOOP AND FOR LOOP
#WHILE LOOP
"""It is a condition expression"""
#Example
"""while condition expression:
          DO something
          Do something
          Do something"""

#Real work
#Print 1 to 5
#Using print function
"""print(1);
print(2);
print(3);
print(4);
print(5);"""

#Using while loop

counter = 1

while counter <=5:
    print(counter)
    counter = counter + 1

#Print even numbers from 0 to 10
counterTwo = 0
while counterTwo <= 10:
    print(counterTwo)
    counterTwo = counterTwo + 2

#print even numbers 0 to 10 using the best Method
counterThree = 0
while counterThree <=10:
    if counterThree%2 == 0:
        print(counterThree)
    counterThree = counterThree + 1

#Reading from an array
numbers = [76,343,11,37,9,6,5]

arrayCount = len(numbers)
countFour = 0
while countFour < arrayCount:
    print(numbers[countFour])
    countFour = countFour + 1

#Getting sum of arrays using loops

arraynumbers = [76,343,11,37,9,6,5]
arrayCount =len(arraynumbers)
count5 = 0
sum = 0
while count5 < arrayCount:
    sum += arraynumbers[count5]
    count5 += 1
print("The array sumis:",sum)

#Multiplication
count6 = 0
product = 1
while count6 < arrayCount:
    product *= arraynumbers[count6]
    count6 += 1
print("The product is:",product)

#trial
x = 0
sum = 1
while x < 10:
    sum+=x
    x = x+1
    
print("OK:",sum)