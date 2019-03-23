# # Paul Caulfield, 2019
# My program reads in a text file and outputs every second line. 
# The program takes the filename of the textfile from an argument on the command line.

                    
with open("moby-dick.txt", 'r') as f:
 # Opens text file "moby-dick.txt" saved in the pands-problem-set directory, the file is opened in read only
# f = text which is read by the program

    
    count = 1
    # Index value is set to 1
    for line in f:
            if not line.isspace():
            # If line is not a blank line adapted from https://stackoverflow.com/a/2369538
                count = count + 1
                # Add 1 to index value
                # adapted program from solution found in https://stackoverflow.com/a/44425842
                  
                if count % 2 == 0:
                # Argument to test if count of line number is divisible by 2 with no remainder
                # As every secound line will have a count which is an even number, it will be divisible by 2 with no remainder.
        
                    print(line)
                    # Print line if argument is true, if false, go to next line
            
                    f.closed 
                    # File is now closed   