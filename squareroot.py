# Paul Caulfield, 2019
# My program takes a positive floating point number as input and outputs an approximation of its square root

x = float(input("Please enter a positive number: "))
# x is the value input by the user, converted into decimat using float data type, ref https://docs.python.org/3.3/library/stdtypes.html 
import math
# https://www.geeksforgeeks.org/python-math-function-sqrt/
z = x + 0

y = (round(math.sqrt(z),1))
# sqrt() function is an inbuilt function in Python programming language that returns the square root of any number.
print("The square root of ",x," is approx.",y,".")
# prints the solution
