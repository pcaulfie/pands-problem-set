# Paul Caulfield, 2019
# My program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

for i in range(1000, 2000):
        if i % 6 == 0: 
        ## and i % 12 != 0:
            print(i)
        else:
            print(i, "is not divisible by 6")
    