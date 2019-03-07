# Paul Caulfield, 2019
# My program outputs whether or not today is a day that begins with the letter T.

import datetime

if datetime.datetime.today().weekday() == 1:
  print("Yes - today begins with a T.")
elif datetime.datetime.today().weekday() == 3:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")