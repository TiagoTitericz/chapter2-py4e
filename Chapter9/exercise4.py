'''Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

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
    if line[0]== 'From':
        dct_day[line[1]] = dct_day.get(line[1], 0) + 1

max_numb = None
for key in dct_day:
    if max_numb == None:
        max_numb = dct_day[key]
        min_numb = dct_day[key]
    elif dct_day[key] > max_numb:
        max_numb = dct_day[key]
        max_person = key
            
print(max_person, max_numb)