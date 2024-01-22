#STORE CARS
#SINGLE DIMENSION ARRAY
cars = ["Ford","Volvo","BMW"]
print(cars[1])

#Finding size of array
print(len(cars))

#Renaming an array
cars[0] = "Toyota"
print(cars[0])

#Add new array to the list
cars.append("Mercedes Benz")
print(cars)

#To remove an element from a list
cars.remove("Volvo")
print(cars)


#NUMBERS
numbers = [67,23,45,90,76,54]
#GETTING SUM
sum = numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]+numbers[5]
print(sum)
#OTHER WAYS
numbers.pop(1)

#MULTIPLE DIMENSION ARRAY
"""1,2,3
5,6,7
8,9,10"""

#STORING
matrix = [[2,3,4],[5,6,7],[8,9,10]]
print(matrix[1][1])

#SUM OF MULTIPLE DIMENSION ARRAY
sumation = matrix[0][0]+matrix[0][1]+matrix[0][2]+matrix[1][0]+matrix[1][1]+matrix[1][2]+matrix[2][0]+matrix[2][1]+matrix[2][2]
print(sumation)