import re

fname = input('Enter a file: ')

fhand = open(fname)
listy = list()
count = 0
for line in fhand:
    x = re.findall('[0-9]+', line)
    for y in range(len(x)):
        number = int(x[y])
        listy.append(number)
        count += 1
        
print(sum(listy))
print(count)