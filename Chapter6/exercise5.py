'''Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.'''

#First way
str = 'X-DSPAM-Confidence:0.8475'
pos = str.find(':')
portion = float(str[pos+1:])
print(portion, type(portion))

'''#Second way
str = 'X-DSPAM-Confidence:0.8475'
portion = float(str[str.find(':')+1:])
print(portion, type(portion))'''