# Paul Caulfield, 2019
# My program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

for i in range(1000, 10000):
    # i is the variable: i is contained in a range of numbers between 1000 and 10000
        if (i % 6 == 0) and (i % 12 != 0):
            # The argument is true if i can be divided by 6 but not 12
                # condition i % 6 == 0 is true when i can be divided by 6 with no remainder, 
                # condition i % 12 != 0 is true when i divided by 12 gives a remainder,
                # both conditions must be met for argument to be true, so I joined them together using "and" function, as 
            print(i)
            # print i if argument is true
        else:
            continue
            # if argument is false, that is where i fails to meet both conditions, then continue with the next iteration of the loop
                           