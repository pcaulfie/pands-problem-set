# Paul Caulfield, 2019
# My program takes a user input string and outputs every second word.

x=input("Please enter a sentance: ")
for word in x.split()[::2]:
    print(word)