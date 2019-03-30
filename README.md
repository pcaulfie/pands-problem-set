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
3. Create while loop which adds the value of x to the variable "total".
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
1. Import the datetime module to retrieve the current date. Source: https://www.w3schools.com/python/python_datetime.asp.
2. If Statement is used to test if today is Tuesday.
3. Function datetime.datetime.today  is used to find what day of week is today,source https://www.pythonforbeginners.com/basics/python-datetime-time-examples.
4. Function datetime.weekday() return the day of the week as an integer, where Monday is 0 and Sunday is 6, source https://docs.python.org/2/library/datetime.html.
5. Argument is true if today is Tuesday, where Tuesday is represented by integer 1.
6. If argument is true print("Yes - today begins with a T.").
7. The print() function writes the quotation when argument is true.
8. ELIF Statement is used to test if today is Thursday.
9. Argument is true if today is Thursday, where Thursday is represented by integer 3.
10. If argument is true print("Yes - today begins with a T.").
11. ELSE statement is used where today is neither Tuesday or Thursday, ie weekday corresponding to today is neither 1 or 3.
12. Prints("No - today does not begin with a T.").


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
1. Define the variable "i" : i is contained in a range of numbers between 1000 and 10000.
2. Use For loop to test which numbers in range fulfil the conditions of the argument.
3. Define The argument is true if i can be divided by 6 but not 12.
4. Define 1st condition: argument is true if i can be divided by 6 with no remainder.
5. Define 2nd condition:  argument is true when i divided by 12 gives a remainder.
6. Both conditions must be met for argument to be true, hence "and" function.
7. Print i if argument is true.
8. If agument is false, continue to test argument with next value in range which becomes new value for i.

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
1. x is the value input by the user. 
2. INT will return an integer object constructed from a number or string x input by the user, reference: https://docs.python.org/3/library/functions.html?highlight=int#int.
3. If user enters a value which is not a positive integer, print message to user to input another number.
4. If number input is a postive integer,  the program will proceed to calculate the sequence.
5. The list [x] will be used to store the value input by the user.
6. The while loop executes as long as the condition (here: x > 1) remains true.
7. Test to see if x is an even number, that is a number which divides by 2 with no remainder.
8. If condition above is true, divide x by 2. The product of which becomes the new value for x.
9. Append the new value for x to the list.
10. Continue with the next iteration of the loop using the new value for x.
11. If condition above is not met, then x is an odd number.
12. Multiply x by 3 and add 1. The product of which becomes the new value for x.
13. Append the new value for x to the list.
14. Then continue with the next iteration of the loop using the new value for x.
15. Output list of values, containing the original input value and the successive values which have been calculated by the program.

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
1. x is the value input by the user. 
2. INT will return an integer object constructed from a number or string x input by the user. https://docs.python.org/3/library/functions.html?highlight=int#int.
3. If user enters a value which is not a positive integer, print message advising user to input another number.
4. User has input a positive integer, so condition is met and the program will proceed to check if the number is a prime.
5. y will equal the count of factors of the number x. y is set to zero to begin with.
6. A prime number is a whole number greater than 1 whose only factors are 1 and itself, therefore number of factors = 2 ie Y = 2.
7. A factor is a whole numbers that can be divided evenly into another number. source: https://whatis.techtarget.com/definition/prime-number.
8.  i = range of positive numbers greater than 1 and less than x.
9. If x can be divided by i with no remainder, this is a factor of the number x.
10. If i is a factor of x, the add 1 to the count of factors for the number x.
11. Continue with the next iteration of the loop using the next value for i.
12. If count of factors = 0, then the program was unable to find any other factors of x (except itself and 1, which are not in the range)Therefore the number x is a prime number.
13. Print result if argument is true.
14. As the count of factors is more than 0, which means that x is divisible by numbers other than itself and one.
15. Print("That is not a prime.").
       
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
1. x is the string input by the user. 
2. Split sentence "x" into words using whitespace as the delimiter - reference https://www.geeksforgeeks.org/python-string-split/
3. [::2] extracts every second word in the list beginning with the first word- reference https://docs.python.org/2.3/whatsnew/section-slices.html.
4. Join every second word with whitespace between each word to form new sentence - adapted from https://stackoverflow.com/a/17645386.
5. Adapted code from https://stackoverflow.com/a/17645629.
6. Print(secondword) will output new sentence containing every second word of the original sentence.

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
1. x is the value input by the user, converted into decimal using float data type, ref https://docs.python.org/3.3/library/stdtypes.html 
2. In order to use sqrt() function, i imported Math Module, ref: https://www.geeksforgeeks.org/python-math-function-sqrt/.
3. z is the value of x plus zero, this is used so that the value of x remains constant and can be printed in the output, while the value z will be used to calculate the square root.
4. y is used to store the value of the square root of z(where z = x), rounded to 1 place decimal.
5. sqrt() function is an inbuilt function in Python programming language that returns the square root of any number.
6. round(number,1) is used to round the product to 1 place decimals - ref https://www.programiz.com/python-programming/methods/built-in/round.
7. Prints the solution.

```
Link to Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/squareroot.py
```

### Problem 8. Write a program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm”.

```
$ python datetime.py
Monday, January 10th 2019 at 1:15pm
```
Overview of Solution
1. Import the datetime module to retrieve the current date. Source: https://www.w3schools.com/python/python_datetime.asp
now = datetime.datetime.now()
2. Create a variable called now which is used to store the current date & time
3. Datetime.datetime.now() gives the current date and time. Reference https://stackoverflow.com/a/4538034
4. Prints a string representing the variable "now", strfttime formats "now" into a string using format codes (directives)
5. Reference for list of formatting directives found at #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
6. %A	Weekday as full name.	Sunday, Monday, …, Saturday 
7. %B	Month as full name. January, February, …, December
8. %d	Day of the month as a zero-padded decimal number.	01, 02, …, 31
9. %Y	Year with century as a decimal number.
10. %I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, …, 12
11. %M	Minute as a zero-padded decimal number.	00, 01, …, 59
12. %p	Locale’s equivalent of either AM or PM.	AM, PM (en_US);

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
1. Open text file "moby-dick.txt" saved in the pands-problem-set directory, the file is opened in read only.
2. Variable "f" equals text which is read by the program.
3. Define Index value called "Count" which is set to 1 : adapted from https://stackoverflow.com/a/30551984.
4. Define variable called "line" in f.
5. Test if line is not a blank line ie string does not consists of whitespace ref https://www.tutorialspoint.com/python/string_isspace.htm.
6. If true, add 1 to index value "count".
7. Argument to test if count of line number is divisible by 2 with no remainder # adapted program from solution found in https://stackoverflow.com/a/44425842.
8. As every secound line will have a count which is an even number, it will be divisible by 2 with no remainder.
9. Print line if argument is true, if false, go to next line.
10. The file is now closed.

```
Link to solution : https://github.com/pcaulfie/pands-problem-set/blob/master/second.py
```

### Problem 10. Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

```

Overview of Solution
1. Import tmatplotlib.pyplot as plt  - adapted program from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
2. Define the x-axis and corresponding y-axis values as lists for each line to be plotted:
3. In order to display 3 lines on same graph. I differentiate between them by giving them a name(label) 
4. 1 line for each function.
5. Define list called "x" containing list of numbers in range [0,4]
6. DEFINE LINE 1 POINTS
7. x axis values containing input value of x1 where x1 = x
8. y axis value contains value of y1, where y1 = x
9. Plot the line 1 points using plt.plotfunction
10. DEFINE LINE 2 POINTS
11. x axis value = x2 where x2 = x
12. y axis value, the square of the values in x, adapted from https://www.quora.com/How-do-I-square-numbers-in-a-list-in-Python
13. Plot the line 2 points using plt.plotfunction 
14. DEFINE LINE 3 POINTS 
15. x axis values = X3 where x3 = x
16. y axis value, y3= [2*i for i in x]
17. Plot the line 3 points using plt.plotfunction 
18. Name the x axis using .xlabel() function.
19. Nameg the y axis using .ylabel() function.
20. Give a title to my plot using .title() function.
21. Display legend on the plot using .legend() function.
22. Display the plot, using .show() function.

```
Link to solution : https://github.com/pcaulfie/pands-problem-set/blob/master/displayplot.py
```
