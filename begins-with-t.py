# Paul Caulfield, 2019
# My program outputs whether or not today is a day that begins with the letter T.

import datetime
# Import the datetime module to retrieve the current date. Source: https://www.w3schools.com/python/python_datetime.asp
if datetime.datetime.today().weekday() == 1:
    # function datetime.datetime.today  is used to find what day of week is today, source https://www.pythonforbeginners.com/basics/python-datetime-time-examples
    # function datetime.weekday() return the day of the week as an integer, where Monday is 0 and Sunday is 6, source https://docs.python.org/2/library/datetime.html
    # "funtion == 1" - argument is true if today is Tuesday, where Tuesday is represented by integer 1
 print("Yes - today begins with a T.")
 # The print() function writes the quotation when argument is true
elif datetime.datetime.today().weekday() == 3:
    # "funtion == 3" - argument is true if today is Thursday, where Thursday is represented by integer 3
  print("Yes - today begins with a T.")
  # The print() function writes the quotation when argument is true
else:
  print("No - today does not begin with a T.")
  # The print() function writes the quotation when argument is false