price = float(input("Enter the price of the item:"))
discount_percentage = float(input("Enter the discount percentage: "))

def calculate_discount(price, discount_percentage):
    if discount_percentage > 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
print(f"The final price after discount is: {calculate_discount(price, discount_percentage)}")
# The code calculates the final price of an item after applying a discount.