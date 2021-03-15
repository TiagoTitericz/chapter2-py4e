'''Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756'''

import re

fname = input('Enter a file: ')

fhand = open(fname)
listy = list()
for line in fhand:
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        number = int(x[0])
        listy.append(number)

print(int(sum(listy) / len(listy)))