# Paul Caulfield, 2019
# My program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm"

import datetime
# Import the datetime module to retrieve the current date. Source: https://www.w3schools.com/python/python_datetime.asp
now = datetime.datetime.now()
# create a variable called now which is used to store the current date & time
# datetime.datetime.now() gives the current date and time. Reference https://stackoverflow.com/a/4538034
print (now.strftime("%A, %B %dth %Y at %I:%M%p")) 
# Prints a string representing the variable "now", strfttime formats "now" into a string using format codes (directives)
# Reference for list of formatting directives found at #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# %A	Weekday as full name.	Sunday, Monday, …, Saturday 
# %B	Month as full name. January, February, …, December
# %d	Day of the month as a zero-padded decimal number.	01, 02, …, 31
# %Y	Year with century as a decimal number.
# %I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, …, 12
# %M	Minute as a zero-padded decimal number.	00, 01, …, 59
# %p	Locale’s equivalent of either AM or PM.	AM, PM (en_US);