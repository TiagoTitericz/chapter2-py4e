# Python For Everybody py4e by Charles Severance

## Chapter 2

## Chapter 3 - Conditions

## Chapter 4 - Functions

Void Functions
Void functions might display something on the screen or have some other effect,
but they don’t have a return value. If you try to assign the result to a variable,
you get a special value called None.
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None

Fruitful Functions
To return a result from a function, we use the return statement in our function.
For example, we could make a very simple function called addtwo that adds two
numbers together and returns a result.

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

Summary
Functions
Built-In Functions
Type conversion (int, float)
String conversions
Parameters
Arguments
Results (fruitful functions)
Void (non-fruitful) functions
Why use functions?

## Chapter 5 - Loop Iterations

Logical Operators - Is and Is Not
Dont´t use Is or Is Not with Integer, Float or Strings variables types. Use them only for None and Boolean variables types


Summary
While loops (indefinite)
Infinite loops
Using break
Using continue
None constants and variables
For loops (definite)
Iteration variables
Loop idioms
Largest or smallest

## Chapter 6 - Strings

Summary
String type
Read/Convert
Indexing strings []
Slicing strings [2:4]
Looping through strings with for and while
Concatenating strings with  +
String operations 
String library
String comparisons
Searching in strings
Replacing text
Stripping white space

## Chapter 7 - Files

Summary
Secondary storage
Opening a file - file handle
File structure - newline character
Reading a file line by line with a for loop
Searching for lines
Reading file names
Dealing with bad files

## Chapter 8 - Lists
- Most list methods are void; they modify the list and return None. Example  t = t.sort() return an error
- Deleting elements:
pop: modifies the list and returns the element that was removed. Ex: x = t.pop(1)
del: If you don't need the removed value, you can use the del operator. Ex: del t[1]    
remove: The return value from remove is None. Ex: t.remove('b')
- Adding elements
t = [1, 2, 3, 4]
print(t) #[1, 2, 3, 4]

t.append(5) #RIGHT
t = t + [5] #RIGHT
print(t) #[1, 2, 3, 4, 5]

t.append([5]) #WRONG! A NESTED LIST WILL BE ADDED O THE t LIST
#[1, 2, 3, 4, [5]]

t = t.append(5) #WRONG! None will be printed out

t + [5] # WRONG! Nothing happen here

t = t + 5 # WRONG! A integer cant´t be concatened with lists

Summary
Concept of a collection
Lists and definite loops
Indexing and lookup
List mutability
Functions: len, min, max, sum
Slicing lists
List methods: append,  remove
Sorting lists
Splitting strings into lists of words
Using split to parse strings

Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.

Exercise 2: Figure out which line of the above program is still not
properly guarded. See if you can construct a text file which causes the
program to fail and then modify the program so that the line is properly
guarded and test it to make sure it handles your new text file.

Exercise 3: Rewrite the guardian code in the above example without
two if statements. Instead, use a compound logical expression using
the or logical operator with a single if statement.

Exercise 4: Find all unique words in a file

Shakespeare used over 20,000 words in his works. But how would you
determine that? How would you produce the list of all the words that
Shakespeare used? Would you download all his work, read it and track
all unique words by hand?

Let’s use Python to achieve that instead. List all unique words, sorted
in alphabetical order, that are stored in a file romeo.txt containing a
subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
Create a list of unique words, which will contain the final result. Write
a program to open the file romeo.txt and read it line by line. For each
line, split the line into a list of words using the split function. For
each word, check to see if the word is already in the list of unique
words. If the word is not in the list of unique words, add it to the list.

When the program completes, sort and print the list of unique words
in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

Exercise 5: Minimalist Email Client.

MBOX (mail box) is a popular file format to store and share a collection
of emails. This was used by early email servers and desktop apps.
Without getting into too many details, MBOX is a text file, which
stores emails consecutively. Emails are separated by a special line which
starts with From (notice the space). Importantly, lines starting with
From: (notice the colon) describes the email itself and does not act as
a separator. Imagine you wrote a minimalist email app, that lists the
email of the senders in the user’s Inbox and counts the number of emails.

Write a program to read through the mail box data and when you find
line that starts with “From”, you will split the line into words using the
split function. We are interested in who sent the message, which is the
second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each
From line, then you will also count the number of From (not From:)
lines and print out a count at the end. This is a good sample output
with a few lines removed:

python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
[...some output removed...]
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word

Exercise 6: Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0

## Chapter 9 - Dictionaries

Summary
What is a collection?
Lists versus Dictionaries
Dictionary constants
The most common word
Using the get() method
Hashing, and lack of order
Writing dictionaries loops
Sneak peek: tuples
Sorting dictionaries

Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.

Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
Sample Line:

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195

Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

## Chapter 10 - Tuples

Summary
Tuple syntax
Immutability
Comparability
Sorting
Tuples in assignment statements
Sorting dictionaries by either key or value

Exercise 1: Revise a previous program as follows: Read and parse the
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
zqian@umich.edu 195

Exercise 2: This program counts the distribution of the hour of the day
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
19 1

Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.

## Chapter 11 - Regular Expressions

Summary
- Regular expressions are a cryptic but powerful language for matching strings and extracting elements from those strings
- Regular expressions have special characters that indicate intent

Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^Xmbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$

Exercise 2: Write a program to look for lines of the form:

New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.
Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756

## Chapter 12 - Networked Programs

Summary
- The TCP/IP gives us pipes / sockets between applications
- We designed application protocols to make use of these pipes
- HyperText Transfer Protocol (HTTP) is a simple yet powerful protocol
- Python has good support for sockets, HTTP, and HTML parsing
