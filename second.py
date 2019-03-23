# # Paul Caulfield, 2019
# My program reads in a text file and outputs every second line. 
# The program takes the filename of the textfile from an argument on the command line.

# Opens filename saved in the pands-problem-set directory, the file is opened in read only
#     
with open("moby-dick.txt", 'r') as f:
            # adapted program from solution found in https://stackoverflow.com/a/44425842
    for count, line in enumerate(f, start=1):
    # counts the number of lines in f, starting at 1
        if count % 2 == 0:
        # Define argument; if count of line number is divisible by 2 with no remainder
            print(line)
            # Print line if argument is true, if false, go to next line
            
            f.closed 
            # File is now closed   