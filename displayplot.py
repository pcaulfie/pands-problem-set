# Paul Caulfield, 2019
# My program displays a plot of the functions x, x² and 2ˣ in the range [0, 4].
# Superscrip characters copied from https://stackoverflow.com/a/51051975

# x & y values 
x1 = list(range(5))
y1= [x1*0 for x1 in range(5)]

x2 = list(range(5))
y2= [x2**x2 for x2 in range(5)]

x3 = list(range(5))
y3= [2*x3 for x3 in range(5)]
print(x1)
print(y1)
print(x2)
print(y2)
print(x3)
print(y3)