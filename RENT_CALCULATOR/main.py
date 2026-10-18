from datetime import datetime
now = datetime.now()
import os

monthly_rent =0
Main_charges =0
park_charges =0
discount =0
UtilityEx =0

name = "GUPTA PROPERTIES"
tname = "Kundan Gupta"

def MonthlyRent():
    print("╔══════════════════════════════════════════╗")
    print("║           MONTHLY RENT CALCULATOR        ║")
    print("╚══════════════════════════════════════════╝")
    global monthly_rent
    global Main_charges
    global park_charges
    global discount
    try:
        monthly_rent = float(input("Enter base monthly rent       : "))
    except:
        print("Invalid Input!")
        monthly_rent = 0
    try:
        Main_charges = float(input("Enter maintenance charges     : "))
    except:
        print("Invalid Input!")
        Main_charges = 0
    try:
        park_charges = float(input("Enter parking charges         : "))
    except:
        print("Invalid Input!")
        park_charges = 0
    try:
        discount = float(input("Enter discount (if any)       : "))
    except:
        print("Invalid Input!")
        discount = 0
    total = (monthly_rent+Main_charges+park_charges)-discount 
    
    print("--------------------------------------------\n\t\tRENT BREAKDOWN\n-------------------------------------------")
    print(f"Base Rent                     : ₹ {monthly_rent:.2f}")
    print(f"Maintenance Charges           : ₹ {Main_charges:.2f}")
    print(f"Parking Charges               : ₹ {park_charges:.2f}")
    print(f"Discount                      : ₹ -{discount:.2f}")

    print("--------------------------------------------")
    print(f"TOTAL MONTHLY RENT             : ₹{total}")
    print("--------------------------------------------")

    print("\n\nRent calculation completed successfully!\n\n")
    #saving data in text file:--
    # with open("p.txt", "w") as f:
    #     f.write(f"{monthly_rent}\n")
    #     f.write(f"{Main_charges}\n")
    #     f.write(f"{park_charges}\n")
    #     f.write(f"{discount}\n")
    
def SplitRent():
    print("╔══════════════════════════════════════════╗")
    print("║            RENT SPLIT CALCULATOR         ║")
    print("╚══════════════════════════════════════════╝")
    try:
        total_rent = float(input("Enter total rent       : "))
    except:
        print("Invalid Input!")
        return
    try:
        tenants = int(input("Enter number of tenants: "))
    except:
        print("Invalid Input!")
        return
    if tenants>0:
        MPT  = (total_rent/tenants)
    else:
        print("tenants cannot be negative!")
        tenants = 0
        MPT = total_rent
    print("--------------------------------------------\n\t\tSPLIT SUMMARY\n-------------------------------------------")
    print(f"Total Monthly Rent     : ₹{total_rent:.2f}")
    print(f"Number of Tenants      : {tenants}")
    print("--------------------------------------------")
    for i in range(1,tenants+1):
        print(f"Tenant {i}               : ₹ {MPT}") #money per tenants
    print("--------------------------------------------")
    print(f"Rent Per Tenant        : ₹ {MPT:.3f}")
    print("--------------------------------------------")
    print(f"Each tenant must pay ₹{MPT:.3f} per month.\n\n")
    
def UtilityExpences():
    print("╔══════════════════════════════════════════╗")
    print("║           UTILITY EXPENSES               ║")
    print("╚══════════════════════════════════════════╝")
    global UtilityEx
    try: 
        ele_bill = float(input("Enter electricity bill    :"))
    except:
        print("invalid input!!")
        ele_bill = 0
    try: 
        water_bill = float(input("Enter water bill          :"))
    except:
        print("invalid input!!")
        water_bill = 0
    try: 
        data_bill = float(input("Enter internet bill       :"))
    except:
        print("invalid input!!")
        data_bill = 0
    try: 
        gas_bill = float(input("Enter gas bill            :"))
    except:
        print("invalid input!!")
        gas_bill = 0
    try: 
        others = float(input("Enter other expenses      :"))
    except:
        print("invalid input!!")
        others = 0
    UtilityEx = ele_bill+water_bill+data_bill+gas_bill+others
    print("--------------------------------------------\n\t\tEXPENSE SUMMARY\n-------------------------------------------")
    print(f"Electricity               : ₹  {ele_bill:.2f}")
    print(f"Water                     : ₹  {water_bill:.2f}")
    print(f"Internet                  : ₹  {data_bill:.2f}")
    print(f"Gas                       : ₹  {gas_bill:.2f}")
    print(f"Other Expenses            : ₹  {others:.2f}")
    print("--------------------------------------------")
    print(f"TOTAL UTILITIES            : ₹{UtilityEx}")
    print("--------------------------------------------")


    print("\nMonthly utility expenses calculated!\n\n")
    
def RentSummary():
    global name
    global tname
    global monthly_rent
    global park_charges
    global discount
    global UtilityEx

    print(f"property Name: {name}")   
    print(f"Tenant Name: {tname}")   
    print("Billing Month: ",end = " ")
    print(now.strftime("%B %Y\n")) 
    print("--------------------------------------------")  
    print("             PAYMENT DETAILS")  
    print("--------------------------------------------") 
 
    print(f"Base Rent           : ₹{monthly_rent}")
    print(f"Maintenance         : ₹{Main_charges}")
    print(f"Parking             : ₹{park_charges}")
    print(f"Discount            : ₹{discount}")
    print(f"Utility Expenses    : ₹{UtilityEx}")
    t =(monthly_rent+Main_charges+park_charges+UtilityEx)-discount
    print("--------------------------------------------") 

    print(f"TOTAL AMOUNT DUE    : ₹{t}")

    print("--------------------------------------------\n\n") 
    print("Payment Status      : UNPAID")
    print("Payment Deadline    : ",end = "")
    print(now.strftime("%d %B %Y"))
    print("\n\n--------------------------------------------\n")
    Summary() 

def LateFee():
    print("╔══════════════════════════════════════════╗")
    print("║            LATE FEE CALCULATOR           ║")
    print("╚══════════════════════════════════════════╝")
    try: 
        pend_rent = float(input("Enter pending rent       :"))
    except:
        print("invalid input!!")
        pend_rent = 0
    try: 
        overdue = int(input("Enter days overdue       :"))
    except:
        print("invalid input!!")
        overdue = 0
    try: 
        threshold = int(input("Enter late fee threshold :"))
    except:
        print("invalid input!!")
        threshold = 0
    try: 
        fixed = float(input("Enter fixed late fee     :"))
    except:
        print("invalid input!!")
        fixed = 0

    if overdue>threshold:
        pend_rent += fixed
     
    print("--------------------------------------------")
    print("              LATE PAYMENT REPORT")
    print("--------------------------------------------")
    print(f"Pending Rent             : ₹{pend_rent:.2f}")
    print(f"Days Overdue             : {overdue} days")
    print(f"Grace Period             : {threshold} days")
    print(f"Late Fee                 : ₹{fixed:.2f}")
    print("--------------------------------------------")
    print(f"TOTAL AMOUNT PAYABLE     : ₹{pend_rent}")
    print("--------------------------------------------")

    print("\nStatus: LATE PAYMENT FEE APPLIED\n\n")

def AnnualRent():
    print("╔══════════════════════════════════════════╗")
    print("║            ANNUAL RENT PROJECTION        ║")
    print("╚══════════════════════════════════════════╝")
    try: 
        monthly_rent = float(input("Enter current monthly rent : "))
    except:
        print("invalid input!!")
        monthly_rent = 0
    
    try: 
        inc = float(input("Enter annual increase (%)  :"))
    except:
        print("invalid input!!")
        inc = 0
    annual = 12*monthly_rent
    tannual = annual + ((annual*5)/100)
    print("--------------------------------------------")
    print("              YEARLY PROJECTION")
    print("--------------------------------------------")
    print(f"\nCurrent Monthly Rent       : ₹{monthly_rent}")
    print(f"Current Annual Rent        : ₹{annual}")
    print(f"Annual Increase             : {inc:.2f}%")
    print("--------------------------------------------")
    print(f"Projected Monthly Rent     : ₹{monthly_rent:.2f}")
    print(f"Projected Annual Rent      : ₹{tannual}")
    print("--------------------------------------------")
    print("Annual Difference          : ₹",tannual-annual)
    print("--------------------------------------------")
    print("\n\nProjection generated successfully!\n")

def Summary():
    global name, tname
    global monthly_rent, Main_charges
    global park_charges, discount, UtilityEx

    billing_month = now.strftime("%B %Y")
    payment_deadline = now.strftime("%d %B %Y")

    total = (
        monthly_rent
        + Main_charges
        + park_charges
        + UtilityEx
        - discount
    )

    summary = f"""
============================================
          RENTWISE MANAGEMENT
             RENT SUMMARY
============================================

Property Name       : {name}
Tenant Name         : {tname}
Billing Month       : {billing_month}

--------------------------------------------
PAYMENT DETAILS
--------------------------------------------
Base Rent           : Rs. {monthly_rent:.2f}
Maintenance         : Rs. {Main_charges:.2f}
Parking             : Rs. {park_charges:.2f}
Discount            : Rs. {discount:.2f}
Utility Expenses    : Rs. {UtilityEx:.2f}

--------------------------------------------
TOTAL AMOUNT DUE    : Rs. {total:.2f}
--------------------------------------------

Payment Status      : UNPAID
Payment Deadline    : {payment_deadline}

============================================
"""

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print("Rent summary saved at:", file_path)
    

print("╔══════════════════════════════════════════╗")
print("║          RENTWISE MANAGEMENT             ║")
print("║       Smart Rent Calculator System       ║")
print("╚══════════════════════════════════════════╝")
print("Welcome! Manage rent, bills and payments.")
print("--------------------------------------------\nMAIN MENU\n--------------------------------------------")
op=0
while(op!=7):
    print("[1]  Calculate Monthly Rent\n[2]  Split Rent Between Tenants\n[3]  Calculate Utility Expenses\n[4]  View Monthly Rent Summary\n[5]  Calculate Late Payment Fee\n[6]  View Annual Rent Projection\n[7]  Exit")
    try:
        op = int(input("Enter your choice: "))
    except:
        print("Invalid Input")
    match op:
        case 1:
            MonthlyRent()
        
        case 2:
            SplitRent()
        
        case 3:
            UtilityExpences()
        
        case 4:
            RentSummary()
        
        case 5:
            LateFee()
        
        case 6:
            AnnualRent()
        
        case 7:
            print("╔══════════════════════════════════════════╗")
            print("║              KUNDAN'S CLI                ║")
            print("╚══════════════════════════════════════════╝")
            print("Thank you for using KUNDAN'S CLI!\n\nYour rent calculations are complete.\nExiting application...\n\nGoodbye!")
        
