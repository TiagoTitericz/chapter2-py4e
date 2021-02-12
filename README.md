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

