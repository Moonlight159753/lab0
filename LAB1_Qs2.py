Song = input("Type in the first line of your favourite song")
Song_length = len (Song)

print ("The length of the song is", Song_length)

starting_number= int(input("Enter the starting number"))
Ending_number= int(input("Enter the Ending number"))

x = slice(starting_number,Ending_number)

print (Song[x])
