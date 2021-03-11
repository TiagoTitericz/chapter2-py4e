'''Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1'''

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
        h = line[5].split(':')
        dct_day[h[0]] = dct_day.get(h[0], 0) + 1
    
lst = list()
for key, val in dct_day.items():
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)