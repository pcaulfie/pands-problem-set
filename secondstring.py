# Paul Caulfield, 2019
# My program takes a user input string and outputs every second word.

x=input("Please enter a sentence: ")
# x is the string input by the user. 
secondword = (' '.join(x.split()[::2]))
# splits sentence "x" into words using whitespace as the delimiter - reference https://www.geeksforgeeks.org/python-string-split/
    # [::2] extracts every second word in the list beginning with the first word- reference https://docs.python.org/2.3/whatsnew/section-slices.html
    # join every second word with whitespace between each word to form new sentence - adapted from https://stackoverflow.com/a/17645386
    # Adapted code from https://stackoverflow.com/a/17645629 
print(secondword)
         # Output new sentence containing every second word of the original sentence