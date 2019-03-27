# Paul Caulfield, 2019
# My program displays a plot of the functions x, x² and 2ˣ in the range [0, 4].
# Superscript characters copied from https://stackoverflow.com/a/51051975

# importing the required module - adapted program from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
import matplotlib.pyplot as plt 

# Define the x-axis and corresponding y-axis values as lists for each line to be plotted:
# In order to display 3 lines on same graph. We differentiate between them by giving them a name(label) 
# 1 line for each function.

# Define list called "x" containing list of numbers in range [0,4]
x = list(range(5))

# Define Line 1 points
# x axis values containing input value of x 
x1 = x
# y axis value 
y1= x
# plotting the line 1 points  
plt.plot(x1, y1, label = "Function x")

# Define Line 2 point
# x axis value
x2 = x
# y axis value, the square of the vlues in x, adapted from https://www.quora.com/How-do-I-square-numbers-in-a-list-in-Python
y2= [i**2 for i in x]
# plotting the line 2 points  
plt.plot(x2, y2, label = "Function x²") 

# Define Line 3 points
# x axis values
x3 = x
# y axis value, 
y3= [2*i for i in x]
# plotting the line 3 points  
plt.plot(x3, y3, label = "Function 2ˣ") 

# naming the x axis using .xlabel() function.
plt.xlabel('x - axis') 
# naming the y axis using .ylabel() function.
plt.ylabel('y - axis') 
# giving a title to my plot using .title() function.
plt.title('Plot of Functions x, x², 2ˣ') 
  
# Display legend on the plot using .legend() function.
plt.legend() 
  
# Display the plot, using .show() function.
plt.show()