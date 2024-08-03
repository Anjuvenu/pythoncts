
price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))
tax_percentage = float(input("Enter the tax percentage: "))




def calculate_discounted_price(price, discount_percentage, tax_percentage):
    # calculate discounted price
    discounted_price = price - (price * discount_percentage / 100)

    # calculate tax amount
    tax_amount = discounted_price * tax_percentage / 100

    # calculate final price
    final_price = discounted_price + tax_amount

    return final_price

 
final = calculate_discounted_price(price, discount_percentage, tax_percentage)
print(final)