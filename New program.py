#Number 2
#Function to calculate the monthly installment for each student
def monthlyInstallment():
    x = 3000000
    r = 0.04
    y = 2
    interest = x * r * y
    amount = x + interest
    monthlyInstalment = amount/24
    return monthlyInstalment
monthlyInstalment = monthlyInstallment()
print("The Monthly Installment for each student is:",monthlyInstalment)

#TOTAL AMOUNT OF MONEY EXPECTED BY UNIVERSITY
#MONTHLY TOTAL AMOUNT
countStudent = 1
Eachstudentmonthly_installment = monthlyInstalment
Amount_expected_per_month = 135000
while countStudent in range(47):
    countStudent = countStudent + 1
    Amount_expected_per_month += monthlyInstalment
print("The Total amount the University Expects per month is:",Amount_expected_per_month)
#TOTAL AMOUNT UNIVERSITY EXPECTS PER YEAR
Total_Amount_per_Year = Amount_expected_per_month * 12
print("The Total Amount per Year is:",Total_Amount_per_Year)

#TOTAL AMOUNT AFTER TWO YEARE
Total_Amount_For_Two_Years = Total_Amount_per_Year * 2
print("The total amount for two years is:",Total_Amount_For_Two_Years)

#The profit the University is to make
Amount_loaned_out = 3000000 * 47
Profit_Realized = Total_Amount_For_Two_Years - Amount_loaned_out
print("The profit realized is:",Profit_Realized)












    


