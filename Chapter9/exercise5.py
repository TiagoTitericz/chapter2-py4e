'''Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dct_day = dict()
for line in fhand:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        atpos = line.find('@')
        domain = line[atpos+1:(line.find(' ',atpos))]
        #print(domain)
        dct_day[domain] = dct_day.get(domain, 0) + 1
print(dct_day)
