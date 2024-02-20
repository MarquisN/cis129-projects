# Module 4 Lab-4
# Author: Marquis Neely
# Date: February 19, 2024
# This program calculates as well as displays store bonus and employee bonus based on monthly sales.
# As well as calculating the percent increase in sales, it also determines the store bonus amount according to set criteria
# and calculates employee bonus based on percentage increase in sales. 
# If the highest bonus amounts are achieved (store bonus amount of $600 and employee bonus of $75), it congratulates employees.


# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0   # employee bonus amount
SalesIncrease = 0 # percent of sales increase
prompt =("Enter the monthy sales amount:") # prompt will be a string literal

# This code gets the monthy sales amount

monthlySales = float(input("Enter the percent of increase in sales:"))

# THis code determines the store bonus
if monthlySales >= 110000:
storeAmount = 6000
elif monthySales >= 100000:
storeAmount = 5000
elif monthySales >= 90000:
storeAmount = 4000
elif monthySales >= 80000:
storeAmount = 3000
else:
storeAmount = 0

# This code gets the percent of increase in sales
salesIncrease = float(input("Enter the percent of increase in sales:"))
salesIncrease = salesIncrease / 100

# This code determines the empAmount bonus
if salesIncrease >= .05:
empAmount = 75
elif salesIncrease >= .04:
empAmount = 50
elif salesIncrease >= .03:
empAmount = 40
else:
empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000 ) and (empAmount == 75):
print('Congrats! You have reached the highest bonus amounts possible! ')
