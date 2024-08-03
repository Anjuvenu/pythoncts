cost_price=float(input("Enter th cost price of the bike:"))
          

if cost_price>100000:
    tax=cost_price*0.15
elif cost_price>50000:
    tax=cost_price*0.10
else:
    tax=cost_price*0.05
print(tax)            




















# tax_15=100000
# tax_10=50000
# tax_15_percent=0.15
# tax_10_percent=0.10
# tax_5_percent=0.05

# if cost_price>tax_15:
#     road_tax=cost_price*tax_15_percent
# elif cost_price>tax_10:
#     road_tax=cost_price*tax_10_percent
# else:
#     road_tax=cost_price*tax_5_percent

# print("Road tax to be paid:" +str(road_tax))  