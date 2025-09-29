name = input("Enter your name")
number = int(input("Enter a number"))
if number < 10 :
    for i in range(1,number+1):
        print(name)
else:
    for n in range(0,3):
        print("Too high")