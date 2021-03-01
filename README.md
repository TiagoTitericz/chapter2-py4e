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

