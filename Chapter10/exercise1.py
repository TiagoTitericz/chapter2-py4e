'''Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dct_day = dict()
for line in fhand:
    line = line.split()
    if len(line) == 0:
        continue
    if line[0] == 'From':
        dct_day[line[1]] = dct_day.get(line[1], 0) + 1

lst = list()
for key, val in list(dct_day.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[0:1]:
    print(val, key)