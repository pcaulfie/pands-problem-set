# Paul Caulfield, 2019
# My program takes a positive floating point number as input and outputs an approximation of its square root

x = float(input("Please enter a positive number: "))
# x is the value input by the user, converted into decimal using float data type, ref https://docs.python.org/3.3/library/stdtypes.html 
import math
# in order to use sqrt() function, i imported Math Module, ref: https://www.geeksforgeeks.org/python-math-function-sqrt/
z = x + 0
# z is the value of x plus zero, this is used so that the value of x remains constant and can be printed in the output, while the value z will be used to calculate the square root.
y = (round(math.sqrt(z),1))
# y is used to store the value of the square root of z(where z = x), rounded to 1 place decimal
# sqrt() function is an inbuilt function in Python programming language that returns the square root of any number.
# round(number,1) is used to round the product to 1 place decimals - ref https://www.programiz.com/python-programming/methods/built-in/round
print("The square root of ",x," is approx.",y,".")
# prints the solution
