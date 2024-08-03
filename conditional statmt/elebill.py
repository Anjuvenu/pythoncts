units_cust=int(input("Enter the number of units consumed:"))
first=0
next=5
after=10

if units_cust<=100:
    bill_amount=0
elif units_cust<200:
    bill_amount=(units_cust-100)*next 
else:
    bill_amount=100*next+(units_cust-200)*after  
print("electricity bill:" + str(bill_amount))