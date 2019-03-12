with open('moby-dick.txt') as f:
    for line in f:
        secondword = (' '.join(line.split()[::2]))

        print(secondword)

# def second.py

# text =import moby-dick.txt
# secondword = (' '.join(x.split()[::2]))
# print(secondword)