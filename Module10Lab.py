def check_protect(dollar_amount):
return '{:*>10}'.format(dollar_amount)
amount = input('Enter a dollar amount: ')
print(check_protect(amount))
