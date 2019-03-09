# Paul Caulfield, 2019
# My program asks the user to input any positive integer and 
    # outputs the successive values of the following calculation:
#       # At each step calculate the next value by taking the current value and ;
            # if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
            # The program ends if the current value is one.

x = int(input("Please enter a positive integer: "))
# x is the value input by the user. 
# INT will return an integer object constructed from a number or string x input by the user. https://docs.python.org/3/library/functions.html?highlight=int#int
while x >= 1:
# The while loop executes as long as the condition (here: x >= 1) remains true.
    if x % 2 == 0:
        x  = x // 2
        print(x)
        break
    else:
        if x % 2 != 0:
            x = (x * 3) + 1
            print(x)
