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
