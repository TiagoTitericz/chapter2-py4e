'''Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.'''

fhand = open('Chapter9/words.txt')

words = dict()
count = 0
for line in fhand:
    line = line.split()
    for x in line:
        count += 1
        words[x] = count

while True:        
    search = input('Enter a word: ')
    if search == 'done':
        break
    if search in words:
        print(True)
    else:
        print(False)

