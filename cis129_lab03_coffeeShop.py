# Author: Marquis Neely
# A Receipt for my coffee shop!
# Created the receipt 

# Number of coffees and muffins from the customer
num_coffees = int(input("How many coffees? "))
num_muffins = int(input("How many muffins? "))
# Figure out the subtotal
coffee_price = 5
muffin_price = 4
subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price)
# Figure out the tax (6% of the subtotal)
tax = 0.06
tax_amount = subtotal * tax
# figure out the final price
final_price = subtotal + tax_amount
# Display the receipt
print("\n***************************************")
print("Marquis's Lattes Receipt")
print(f"{num_coffees} Coffee $5 each: ${num_coffees * coffee_price:.2f}")
print(f"{num_muffins} Muffins $4 each: ${num_muffins * muffin_price:.2f}")
print(f"6% tax: ${tax_amount:.2f}")
print("---------")
print(f"Total: ${final_price:.2f}")
print("***************************************")
