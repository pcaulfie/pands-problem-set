# Paul Caulfield, 2019
# My program asks the user to input a positive integer and tells the user whether or not the number is a prime.

x = int(input("Please enter a positive integer: "))
# x is the value input by the user. 
# INT will return an integer object constructed from a number or string x input by the user. https://docs.python.org/3/library/functions.html?highlight=int#int
if x < 1:
# If user enters a value which is not a positive integer, print message below  
    print("Number is not a positive integer; please enter a whole number greater than 0!")
    # Advises user to input another number
else:
# User has input a positive integer, so condition is met and the program will proceed to check if the number is a prime.
    y = 0
    # y will equal the count of factors of the number x.
    # A prime number is a whole number greater than 1 whose only factors are 1 and itself, therefore number of factors = 2 ie Y = 2
    for i in range (2, x):
    # i = range of positive numbers between 1 and x
        if x % i == 0:
        # If x divided by i with no remainder
            y = y + 1
            # if true add 1 to the count of factors for the number x
    if y >= 3:
        print("That is not a prime.")
    else:
        print("That is a prime.")



