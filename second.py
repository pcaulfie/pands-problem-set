# def second(moby-dick.txt):
    
with open("moby-dick.txt") as f:
            # adapted progrm from solution found in https://stackoverflow.com/a/16922328
        for line in f:
        # line is used to store text extracted as f 
            secondword = (' '.join(line.split()[::2]))
            # splits lines of text in textfile into words using whitespace as the delimiter - reference https://www.geeksforgeeks.org/python-string-split/
                # [::2] extracts every second word in the textfile beginning with the first word- reference https://docs.python.org/2.3/whatsnew/section-slices.html
                # join every second word with whitespace between each word to form new list of words - adapted from https://stackoverflow.com/a/17645386
                # Adapted code from https://stackoverflow.com/a/17645629 
            print(secondword)