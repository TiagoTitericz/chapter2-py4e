'''Exercise 1: Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.'''

def chop(t):
    del t[0]
    x = len(t)
    del t[x-1]

def middle(t):
    x = t.pop(0)
    z = len(t)
    y = t.pop(z-1)
    removed_list = list()
    removed_list.append(x)
    removed_list.append(y)
    return removed_list

numblist = list()
while True:
    prompt = input('Enter an element of the list: ')
    if prompt == 'done':
        break
    numblist.append(prompt)

orig_numblist = numblist[:]
#chop(numblist)
removed_list = middle(numblist)
print('The original list:', orig_numblist)
print('The removed elements:', removed_list) 
print('The new list:', numblist)


