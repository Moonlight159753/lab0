Total = 0 
for i in range (0,5):
    number =input("Please enter a number")
    answer = input ("if you want that number included? Yes/No ")
    if answer == "yes":
        Total = Total + number
    break
print(Total)