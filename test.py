# Paul Caulfield, 2019
# My program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm"

from datetime import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))