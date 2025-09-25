Regualr_price = 3.49 
discount = 0.6 

num = int(input("Enter the number of loaves of day old bread"))

discount_price = Regualr_price * discount 

total_price = num * discount_price 

print (f'The discount price is {discount_price:.2f}')
print (f'The total price is {total_price:.2f}')
