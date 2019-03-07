# Paul Caulfield, 2019
# My program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

x = int(input("Please enter a positive integer: "))
# x is the value input by the user. 
# INT will return an integer object constructed from a number or string x input by the user. https://docs.python.org/3/library/functions.html?highlight=int#int

total = 0
# total will be used to store the value of the sum of all numbers between 1 and x. I define it here and give it a value of zero
while x > 0:
    # The while loop executes as long as the condition (here: x > 0) remains true.
    total = total + x
    # The total will be incremented by the value of x
    x = x - 1
# Subtracts 1 from the value of x on each loop as long as the condition (x > 0), this value become the new input value replacing the input value entered by the user and will change with each iteration of the loop until it fails to meet the condition.
print(total)
# The print() function writes the value of the argument(s) it is given, in this case it is the summ of all numbers between 1 and x, where x is a potitive integer entered by the user. https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming