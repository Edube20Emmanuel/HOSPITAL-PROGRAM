#NUMBER ONE
#A PROGRAM TO BE USED FOR BILLG PAIIENTS AT MM HOSPTAL
Services_Offered = ["Consultation","Admission","Lab tests","treatment","Oxygen and ICU"]
print(Services_Offered)
First_Service = input("Enter Service: ")
while First_Service == "Consultation":
    Consultation_Bill = 100000
    print("The Consultation Bill is:",Consultation_Bill)
    print("Is the Condition Major or Minner")
    condition = input("Enter condition: ")
    if condition == "Minner":
        print("Test lab")
        Test_lab_Bill = 50000
        print("Treatment")
        Treatment_Bill = 200000
        print("The treatment Bill is:",Treatment_Bill)
        Total_Amount = Consultation_Bill + Treatment_Bill + Test_lab_Bill
        print("The total Bill is:",Total_Amount)
        print("Make payment")
        Payment = input("Enter Payment: ")
        if Payment == Total_Amount:
            print("Thanks very much")
    elif condition == "Major":
        print("Admission")
        Admission_Bill = 250000
        print("The Admission Bill is:",Admission_Bill)
        print("Test lab")
        Test_lab_Bill = 100000
        print("The Test Lab Bill is:",Test_lab_Bill)
        Total_Amount = Consultation_Bill + Admission_Bill + Test_lab_Bill
        print("The total Bill is:",Total_Amount)
        print("Make payment")
        Payment = input("Make Payment: ")
        print("Enter level of illness")
        illness_Level = input("Enter level of illness: ")
        if illness_Level == "Low":
            print("Give the necessary Treatment")
            Treatment_Bill = 200000
            print("Did the patient pay for the first bills")
            First_Billpayment = input("Did you pay for the first Bills: ")
            if First_Billpayment == "Yes":
                print("Pay only:",Treatment_Bill)
                Payment = input("Make payment: ")
                print("Thanks Very Much")
            elif First_Billpayment == "No":
                print("Make payment of all bills")
                Total_Bill = Total_Amount + Treatment_Bill
                print("The Total Bill is:",Total_Bill)
                Payment = input("Make Payment: ")
            else:
                print("We are sorry you need to Restart the process")
        elif illness_Level == "High":
            print("Proceed to Intensive Care Unit")
            print("Does the patient require only ICU OR ICU and Oxygen")
            Unit_Admitted = input("ENTER Y FOR BOTH AND X FOR ONLY ICU: ")
            if Unit_Admitted == "x":
                ICU_Bill = 1000000
                print("Did the patient pay for the first bills")
                First_Billpayment = input("Did you pay for the first Bills: ")
                if First_Billpayment == "Yes":
                    print("Pay only:",ICU_Bill)
                    Payment = input("Make payment: ")
                elif First_Billpayment == "No":
                    print("Make payment of all bills")
                    Total_Bill = Total_Amount + ICU_Bill
                    print("The Total Bill is:",Total_Bill)
                    Payment = input("Make Payment: ")
            elif Unit_Admitted == "Y":
                ICU_Bill_and_Oxygen_Bill = 2000000
                print("Did the patient pay for the first bills")
                First_Billpayment = input("Did you pay for the first Bills: ")
                if First_Billpayment == "Yes":
                    print("Pay only:",ICU_Bill_and_Oxygen_Bill)
                    Payment = input("Make payment: ")
                elif First_Billpayment == "No":
                    print("Make payment of all bills")
                    Total_Bill = Total_Amount + ICU_Bill_and_Oxygen_Bill
                    print("The Total Bill is:",Total_Bill)
                    Payment = input("Make Payment: ")



        break

while First_Service == "treatment":
    Treatment_Bill = 200000
    print("The treatment Bill is:",Treatment_Bill)
    Payment = input("Make payment: ")
    if(Payment == Treatment_Bill):
        print("Thanks very much")         
            




    

