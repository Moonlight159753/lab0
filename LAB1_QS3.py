firstname = input ("Enter the length of the first name")

firstname_length = len(firstname)
if firstname_length < 5:
    surename = input ("Enter your surename")
    fullname = firstname + surename
    x = fullname.upper()
    print(x)
else:
    y = firstname.lower
    print(y)