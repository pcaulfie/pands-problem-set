# Paul Caulfield, 2019
# My program displays a plot of the functions x, x² and 2ˣ in the range [0, 4].
# Superscrip characters copied from https://stackoverflow.com/a/51051975

# Line 1 points
# x axis values 
x1 = list(range(5))
# y axis value
y1= [i*0 for i in x1]

# Line 2 points
# x axis value
x2 = list(range(5))
# y axis value, the square of the vlues in x, adapted from https://www.quora.com/How-do-I-square-numbers-in-a-list-in-Python
y2= [i**2 for i in x2]

# Line 2 points
# x axis values
x3 = list(range(5))
# y axis value, 
y3= [2*i for i in x3]
print(x1)
print(y1)
print(x2)
print(y2)
print(x3)
print(y3)