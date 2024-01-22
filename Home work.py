def sumnumbers():
    num1 = 80
    num2 = 78
    sum = num1 + num2
    return sum
summation = sumnumbers()
print(summation)

#WHILE LOOPS ARRAY
Marks = [89,84,83,80]
arraycount = len(Marks)
print(arraycount)
count = 0
while count < arraycount:
    print(Marks[count])
    count = count + 1
def sumnumber():
    num3 = input("Ener number: ")
    num4 = input("Ener number: ")
    sum = num3 + num4
    return sum
result = sumnumber()
print("The sum is:",result)

#PROGRAM FOR STUDENTS
print("WELCOME TO MINISTRY OF ICT TUTION SUPPORT")
CoursesRequired = ["Science","Technology","Emgineering","Math"]
Name = input("Enter your name: ")
print("WELCOME TO OUR CHANNEL",Name)
Course = input("Enter course: ")
University = input("Enter University: ")
Tution = int(input("Enter Amount tution: "))
Level = ["Degree","Diploma"]
study_level = input("Enter Level of study: ")
if Course in CoursesRequired:
    Allowance = 200000
    if study_level == "Degree":
        def TotalAmount():
            Amount = Allowance + Tution
            return Amount
        TotalTution = TotalAmount()
        print("The total amount is:UGX",TotalTution)
    elif study_level == "Diploma":
        def TotalAmount():
            Amount = Allowance + 0.5 * Tution
            return Amount
        TotalTution = TotalAmount()
        print("The total tution:UGX",TotalTution)
print("THE MINISTRY OF ICT WISHES YOU A NICE EDUCATION")


        



        


