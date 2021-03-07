# This program will create a key list from a dictonary using the key method. The will sort the is and print key and its
# correspondng value

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.key()) #key method
print(lst)
lst.sort() #sorting the list
for key in lst: #looping through the list and printing it
    print(key, counts[key])
