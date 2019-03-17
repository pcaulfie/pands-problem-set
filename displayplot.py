# Paul Caulfield, 2019
# My program displays a plot of the functions x, x² and 2ˣ in the range [0, 4].
# Superscript characters copied from https://stackoverflow.com/a/51051975

# importing the required module - adapted program from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
import matplotlib.pyplot as plt 

# Line 1 points
# x axis values 
x1 = list(range(5))
# y axis value
y1= [i*0 for i in x1]
# plotting the line 1 points  
plt.plot(x1, y1, label = "Function x")

# Line 2 points
# x axis value
x2 = list(range(5))
# y axis value, the square of the vlues in x, adapted from https://www.quora.com/How-do-I-square-numbers-in-a-list-in-Python
y2= [i**2 for i in x2]
# plotting the line 2 points  
plt.plot(x2, y2, label = "Function x²") 

# Line 2 points
# x axis values
x3 = list(range(5))
# y axis value, 
y3= [2*i for i in x3]
# plotting the line 3 points  
plt.plot(x3, y3, label = "Function 2ˣ") 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Plot of Functions x, x², 2ˣ') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show()