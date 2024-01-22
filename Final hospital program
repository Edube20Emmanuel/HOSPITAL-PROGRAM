#NUMBER ONE
#A PROGRAM TO BE USED FOR BILLG PAIIENTS AT MM HOSPTAL
Services_Offered = ["Consultation","Admission","Lab tests","treatment","Oxygen and ICU"]
print(Services_Offered)
First_Service = input("Enter Service: ")
while First_Service == "Consultation":
    try:
        Consultation_Bill = 100000
        print("The Consultation Bill is:",Consultation_Bill)
        print("You can pay if you wish")
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
            Payment = int(input("Make Payment: "))
            if Payment == 350000:
                print("Thanks very much")
                print("We shall serve you perfectly")
            elif Payment > 350000:
                print("You have paid Extra Money")
                print("Your change is:",Payment - 350000)
            else:
                print("The balance is:",350000 - Payment)
                print("Please complete your Bills to receive our services")
                Payment = int(input("Make Payment: "))
                print("Thank you")
                break
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
            Payment = int(input("Make Payment: "))
            if Payment == 450000:
                print("Thank you very much")
                print("We shall serve you perfectly")
            elif Payment > 450000:
                print("You have paid Extra Money")
                print("Your change is:",Payment - 450000)
            else:
                print("The balance is:",450000 - Payment)
                print("Please complete your Bills to receive our services")
                Payment = int(input("Make Payment: "))
                print("Thank you")
            print("Enter level of illness")
            illness_Level = input("Enter level of illness: ")
            if illness_Level == "Low":
                print("Give the necessary Treatment")
                Treatment_Bill = 200000
                print("Did the patient pay for the first bills")
                First_Billpayment = input("Did you pay for the first Bills: ")
                if First_Billpayment == "Yes": 
                    print("Pay only:",Treatment_Bill)
                    Payment = int(input("Make payment: "))
                    if Payment == 200000:
                        print("Thank you very much")
                        print("We shall serve you perfectly")
                    elif Payment > 450000:
                        print("You have paid Extra Money")
                        print("Your change is:",Payment - 450000)
                    else:
                        print("The balance is:",200000 - Payment)
                        print("Please complete your Bills to receive our services")
                        Payment = int(input("Make balance Payment: "))
                        print("Thank you")    
                elif First_Billpayment == "No":
                    print("Make payment of all bills")
                    Total_Bill = Total_Amount + Treatment_Bill
                    print("The Total Bill is:",Total_Bill)
                    Payment = int(input("Make Payment: "))
                    if Payment == 650000:
                        print("Thank you very much")  
                        print("You will receive our services perfectly")
                    elif Payment > 650000:
                        print("You have payed extra money") 
                        print("Your change is:",Payment - 650000) 
                    else:
                        print("You have paid less Money")
                        print("The balance is:",650000 - Payment)
                        print("Please complete your Bills to receive our services")
                        Payment = int(input("Make balance Payment: "))
                        print("Thank you")    

                else:
                    print("We are sorry you need to Restart the process")
                    break
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
                        Payment = int(input("Make payment: "))
                        if Payment == 1000000:
                            print("Thank you very much")  
                            print("You will receive our services perfectly")
                        elif Payment > 1000000:
                            print("You have payed extra money") 
                            print("Your change is:",Payment - 1000000) 
                        else:
                            print("You have paid less Money")
                            print("The balance is:",1000000 - Payment)
                            print("Please complete your Bills to receive our services")
                            Payment = int(input("Make balance Payment: "))
                            print("Thank you")    
                    elif First_Billpayment == "No":
                        print("Make payment of all bills")
                        Total_Bill = Total_Amount + ICU_Bill
                        print("The Total Bill is:",Total_Bill)
                        Payment = int(input("Make Payment: "))
                        if Payment == 1450000:
                            print("Thank you very much")  
                            print("You will receive our services perfectly")
                        elif Payment > 1450000:
                            print("You have payed extra money") 
                            print("Your change is:",Payment - 1450000)
                        else:
                            print("You have paid less Money")
                            print("The balance is:",1450000 - Payment)
                            print("Please complete your Bills to receive our services")
                            Payment = int(input("Make balance Payment: "))
                            print("Thank you")    

                elif Unit_Admitted == "Y":
                    ICU_Bill_and_Oxygen_Bill = 2000000
                    print("Did the patient pay for the first bills")
                    First_Billpayment = input("Did you pay for the first Bills: ")
                    if First_Billpayment == "Yes":
                        print("Pay only:",ICU_Bill_and_Oxygen_Bill)
                        Payment = input("Make payment: ")
                        if Payment == 2000000:
                            print("Thank you very much")  
                            print("You will receive our services perfectly")
                        elif Payment > 2000000:
                            print("You have payed extra money") 
                            print("Your change is:",Payment - 2000000)
                        else:
                            print("You have paid less Money")
                            print("The balance is:",2000000 - Payment)
                            print("Please complete your Bills to receive our services")
                            Payment = int(input("Make balance Payment: "))
                            print("Thank you")    
                    elif First_Billpayment == "No":
                        print("Make payment of all bills")
                        Total_Bill = Total_Amount + ICU_Bill_and_Oxygen_Bill
                        print("The Total Bill is:",Total_Bill)
                        Payment = int(input("Make Payment: "))
                        if Payment == 2450000:
                            print("Thank you very much")  
                            print("You will receive our services perfectly")
                        elif Payment > 2000000:
                            print("You have payed extra money") 
                            print("Your change is:",Payment - 2450000)
                        else:
                            print("You have paid less Money")
                            print("The balance is:",2450000 - Payment)
                            print("Please complete your Bills to receive our services")
                            Payment = int(input("Make balance Payment: "))
                            print("Thank you")    
                        break
    except ValueError:
        print("Enter only numbers")
    


while First_Service == "Treatment":
    try:
        Treatment_Bill = 200000
        print("The treatment Bill is:",Treatment_Bill)
        Payment = int(input("Make payment: "))
        if Payment == 200000:
            print("Thanks very much")
            print("You will receive our services perfectly")
        elif Payment > 200000:
            print("You have payed extra money") 
            print("Your change is:",Payment - 200000)

        else:
            print("The balance is:", 200000 - Payment)
            print("Please make all your payment to receive our services")
            Payment = int(input("Make balance Payment: "))
            print("Thank you")    
        break
        
    except ValueError:
        print("Enter only numbers")                                             