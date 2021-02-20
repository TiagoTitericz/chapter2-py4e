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



