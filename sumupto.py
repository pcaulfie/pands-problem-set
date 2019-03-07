# Paul Caulfield, 2019
# My program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

x = int(input("Please enter a positive integer: "))



total = 0

while x > 0:
    total = total + x
    x = x - 1

print(total)