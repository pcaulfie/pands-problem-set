# Problem Set 2019

This document contains a brief description of solutions for Problem Set 2019 for Programming and Scripting. There are ten solutions, one for each problem in the problem set.

## Getting Started

I have created a GitHub Repository where you can access my project, its files, and all the versions of its files that Git saves. See link https://github.com/pcaulfie/pands-problem-set

### Problem 1. Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
```
Example
$ python sumupto.py
Please enter a positive integer: 10
55
```
Overview of solution
1. Ask user to enter a positive integer  which I call "x" and format as an integer.  
2. Create a variable called "total" which will store the sum of values between 1 and x, the start value = zero
3. Create while loop which adds the value of x to the varuable "total".
4. The loop continues to subtract 1 from value of x and add this to the "total" while x is greater than 0. 
5. Prints the value stored in variable "total".

```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/sumupto.py
```

### Problem 2. Write a program that outputs whether or not today is a day that begins with the letter T. 

```
An example of running this program on a Thursday is as follows.
$ python begins-with-t.py
Yes - today begins with a T.
An example of running it on a Wednesday is as follows.
$ python begins-with-t.py
No - today does not begin with a T.
```
Overview of solution
1. Import the datetime module to retrieve the current date. Source: https://www.w3schools.com/python/python_datetime.asp
2. If Statement is used to test if today is Tuesday
3 Function datetime.datetime.today  is used to find what day of week is today,source https://www.pythonforbeginners.com/basics/python-datetime-time-examples
4. Function datetime.weekday() return the day of the week as an integer, where Monday is 0 and Sunday is 6, source https://docs.python.org/2/library/datetime.html
5.  Argument is true if today is Tuesday, where Tuesday is represented by integer 1
6. If argument is true print("Yes - today begins with a T.")
7. The print() function writes the quotation when argument is true
8. ELIF Statement is used to test if today is Thursday
9. Argument is true if today is Thursday, where Thursday is represented by integer 3
10. IIf argument is true print("Yes - today begins with a T.")
11. ELSE statement is used where today is neither Tuesday or Thursday, ie weekday corresponding to today is neither 1 or 3
12.   prints("No - today does not begin with a T.")


```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/begins-with-t.py
```

### Problem 3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

```
$ python divisors.py
1002
1014
1026
etc
9990
```
Overview of solution
Define the variable "i" : i is contained in a range of numbers between 1000 and 10000
Use For loop to test which numbers in range fulfil the conditions of the argument
Define The argument is true if i can be divided by 6 but not 12
Define 1st condition: argument is true if i can be divided by 6 with no remainder, 
Define 2nd condition:  argument is true when i divided by 12 gives a remainder,
Both conditions must be met for argument to be true, hence "and" function.
print i if argument is true
If agument is false, continue to test argument with next value in range which becomes new value for i

```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/divisors.py
```

### Problem 4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

```
$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1
```
Overview of solution
1.0 # x is the value input by the user. 
1.1 INT will return an integer object constructed from a number or string x input by the user. https://docs.python.org/3/library/functions.html?highlight=int#int
1.2 If user enters a value which is not a positive integer, print message to user to input another number
2. If number input is a postive integer,  the program will proceed to calculate the sequence.
2.1 The list [x] will be used to store the value input by the user
2.2 The while loop executes as long as the condition (here: x > 1) remains true.
2.3 Test to see if x is an even number, that is a number which divides by 2 with no remainder.
2.4 if condition above is true, divide x by 2. The product of which becomes the new value for x
2.5 append the new value for x to the list
2.6 continue with the next iteration of the loop using the new value for x
3.0 if condition above is not met, then x is an odd number 
3.1 multiply x by 3 and add 1. The product of which becomes the new value for x
3.2 append the new value for x to the list
3.3 then continue with the next iteration of the loop using the new value for x
4.0 Output list of values, containing the original input value and the successive values which have been calculated by the program.

```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/collatz.py
```

### Problem 5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

```
$ python primes.py
Please enter a positive integer: 19
That is a prime.
```

Overview of Solution
1.0 x is the value input by the user. 
1.1 INT will return an integer object constructed from a number or string x input by the user. https://docs.python.org/3/library/functions.html?highlight=int#int
1.2 If user enters a value which is not a positive integer, print message advising user to input another number
2.0 User has input a positive integer, so condition is met and the program will proceed to check if the number is a prime.
2.1 y will equal the count of factors of the number x. y is set to zero to begin with.
2.1.1 A prime number is a whole number greater than 1 whose only factors are 1 and itself, therefore number of factors = 2 ie Y = 2
2.1.2 A factor is a whole numbers that can be divided evenly into another number. source: https://whatis.techtarget.com/definition/prime-number
2.2  i = range of positive numbers greater than 1 and less than x
2.3 If x can be divided by i with no remainder, this is a factor of the number x
2.4 if i is a factor of x, the add 1 to the count of factors for the number x
2.5 continue with the next iteration of the loop using the next value for i
3.0 if count of factors = 0, then the program was unable to find any other factors of x (except itself and 1, which are not in the range)Therefore the number x is a prime number
3.1 print result if argument is true
4.0 As the count of factors is more than 0, which means that x is divisible by numbers other than itself and one
4.1 print("That is not a prime.")
       
```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/primes.py
```

### Problem 6. Write a program that takes a user input string and outputs every second word.

```
$ python secondstring.py
Please enter a sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog
```
Overview of Solution
1.0 x is the string input by the user. 
2.0 split sentence "x" into words using whitespace as the delimiter - reference https://www.geeksforgeeks.org/python-string-split/
2.2 [::2] extracts every second word in the list beginning with the first word- reference https://docs.python.org/2.3/whatsnew/section-slices.html
2.3 join every second word with whitespace between each word to form new sentence - adapted from https://stackoverflow.com/a/17645386
2.4 Adapted code from https://stackoverflow.com/a/17645629 
2.5 print(secondword) will output new sentence containing every second word of the original sentence

```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/secondstring.py
```

### Problem 7. Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

```
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.
```
Overview of Solution
1.0 x is the value input by the user, converted into decimal using float data type, ref https://docs.python.org/3.3/library/stdtypes.html 
1.1 in order to use sqrt() function, i imported Math Module, ref: https://www.geeksforgeeks.org/python-math-function-sqrt/
2.0 z is the value of x plus zero, this is used so that the value of x remains constant and can be printed in the output, while the value z will be used to calculate the square root.
2.1 y is used to store the value of the square root of z(where z = x), rounded to 1 place decimal
2.2 sqrt() function is an inbuilt function in Python programming language that returns the square root of any number.
2.3 round(number,1) is used to round the product to 1 place decimals - ref https://www.programiz.com/python-programming/methods/built-in/round
2.4 prints the solution

```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/squareroot.py
```

### Problem 8. Write a program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm”.

```
$ python datetime.py
Monday, January 10th 2019 at 1:15pm
```
Overview of Solution
1.0 Import the datetime module to retrieve the current date. Source: https://www.w3schools.com/python/python_datetime.asp
now = datetime.datetime.now()
1.1 create a variable called now which is used to store the current date & time
1.2 datetime.datetime.now() gives the current date and time. Reference https://stackoverflow.com/a/4538034
1.3 # Prints a string representing the variable "now", strfttime formats "now" into a string using format codes (directives)
# Reference for list of formatting directives found at #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# %A	Weekday as full name.	Sunday, Monday, …, Saturday 
# %B	Month as full name. January, February, …, December
# %d	Day of the month as a zero-padded decimal number.	01, 02, …, 31
# %Y	Year with century as a decimal number.
# %I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, …, 12
# %M	Minute as a zero-padded decimal number.	00, 01, …, 59
# %p	Locale’s equivalent of either AM or PM.	AM, PM (en_US);

```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/todaysdatetime.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 9. Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

```
$ python second.py moby-dick.txt
Title: Moby Dick; or The Whale
CHAPTER 1
Call me Ishmael. Some years ago--never mind how long
particular to interest me on shore, I thought I would sail about a

```

Overview of Solution
1.0 Open text file "moby-dick.txt" saved in the pands-problem-set directory, the file is opened in read only
1.1 Variable "f" equals text which is read by the program
2.0 Define Index value called "Count" which is set to 1 : adapted from https://stackoverflow.com/a/30551984
2.1 Define variable called "line" in f 
2.1.1 Test if line is not a blank line ie string does not consists of whitespace ref https://www.tutorialspoint.com/python/string_isspace.htm
2.2 if true, add 1 to index value "count"
2.3 Argument to test if count of line number is divisible by 2 with no remainder # adapted program from solution found in https://stackoverflow.com/a/44425842
2.4 As every secound line will have a count which is an even number, it will be divisible by 2 with no remainder.
2.5 Print line if argument is true, if false, go to next line
2.6 The file is now closed 

```
Link to solution : https://github.com/pcaulfie/pands-problem-set/blob/master/second.py
```

### Problem 10. Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

```

Overview of Solution
# importing tmatplotlib.pyplot as plt  - adapted program from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# Define the x-axis and corresponding y-axis values as lists for each line to be plotted:
# In order to display 3 lines on same graph. We differentiate between them by giving them a name(label) 
# 1 line for each function.
# Define list called "x" containing list of numbers in range [0,4]
# Define Line 1 points
# x axis values containing input value of x1 
# y axis value contains value of y1
# plot the line 1 points  
# Define Line 2 point
# x axis value = x2
# y axis value, the square of the values in x, adapted from https://www.quora.com/How-do-I-square-numbers-in-a-list-in-Python
# plotting the line 2 points  
# Define Line 3 points
# x axis values
# y axis value, y3= [2*i for i in x]
# plot the line 3 points  
# naming the x axis using .xlabel() function.
# naming the y axis using .ylabel() function.
# giving a title to my plot using .title() function.
# Display legend on the plot using .legend() function.
# Display the plot, using .show() function.

```
Link to solution : https://github.com/pcaulfie/pands-problem-set/blob/master/displayplot.py
```
