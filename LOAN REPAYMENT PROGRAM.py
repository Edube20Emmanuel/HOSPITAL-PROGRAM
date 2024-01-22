#WHILE LOOPS PRACTISE
#RUTHS PROGRAM
#LOAN REPAYMENT PROGRAM
print("LOAN REPAYMENT PROGRAM")
Name = input("ENTER YOUR NAME: ")
print(Name,"WELCOME TO WHERE LIFE IS SIMPLIFIED")
Principle = int(input("ENTER THE AMOUNT OF LOAN ACQUIRED: "))
Repayment_Amount = int(input("ENTER INSTALLMENT PAYMENTS: "))
Payment_Month = ["JAN","FEB","MAR","APR","MAY","JUN","JULY","AUG","SEPT","OCT","NOV","DEC"]
balance = Principle - Repayment_Amount
arraymonth = len(Payment_Month)
x = balance
while x < 0:
    balance = Principle - x
    print(balance)
    
