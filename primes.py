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
    # y will equal the count of factors of the number x. y is set to zero to begin with.
    # A prime number is a whole number greater than 1 whose only factors are 1 and itself, therefore number of factors = 2 ie Y = 2
    # A factor is a whole numbers that can be divided evenly into another number. source: https://whatis.techtarget.com/definition/prime-number
    for i in range (2, x):
    # i = range of positive numbers greater than 1 and less than x
        if x % i == 0:
        # If x can be divided by i with no remainder, this is a factor of the number x
            y = y + 1
            # i is a factor of x, the add 1 to the count of factors for the number x
            continue
            # continue with the next iteration of the loop using the next value for i
    if y == 0:
    # if count of factors = 0, then the program was unable to find any other factors of x (except itself and 1, which are not in the range)
    # Therefore the number x is a prime number
        print("That is a prime.")
        # Print result if argument is true
    else:
        # The count of factors is more than 0, which means that x is divisible by numbers other than itself and one
        print("That is not a prime.")
        # Print result if argument is false



