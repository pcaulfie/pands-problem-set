# Paul Caulfield, 2019
# My program asks the user to input any positive integer and 
    # outputs the successive values of the following calculation:
#       # At each step calculate the next value by taking the current value and ;
            # if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
            # The program ends if the current value is one.

x = int(input("Please enter a positive integer: "))
# x is the value input by the user. 
# INT will return an integer object constructed from a number or string x input by the user. https://docs.python.org/3/library/functions.html?highlight=int#int
if x < 1:
# If user enters a value which is not a positive integer, I do not want to store this value in my list, so I have set this condition    
    print("Number is not a positive integer; please enter a whole number greater than 0!")
    # Advises user to input another number
else:
# User has input a positive integer, so condition is met and the program will proceed to calculate the sequence.
    list = [x]
    # The list will be used to store the value input by the user
    while x > 1:
    # The while loop executes as long as the condition (here: x > 1) remains true.
    # I did not set condition x >= 1 as this would create an infinite loop.
        if x % 2 == 0:
        # Test to see if x is an even number, that is a number which divides by 2 with no remainder.
            # The condition x % 2 == 0 is true when x can be divided by 2 with no remainder,
            x  = x // 2
            # if condition above is true, divide x by 2. The product of which becomes the new value for x
            list.append(x)
            # append the new value for x to the list
            continue
            # continue with the next iteration of the loop using the new value for x
        else:
        # if condition above is not met, then x is an odd number 
            x = (x * 3) + 1
            # multiply x by 3 and add 1. The product of which becomes the new value for x
            list.append(x)
            # append the new value for x to the list
        continue
        # then continue with the next iteration of the loop using the new value for x
    print(list)
    # Output list of values, containing the original input value and the successive values which have been calculated by the program.