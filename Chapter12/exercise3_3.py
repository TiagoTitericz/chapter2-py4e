'''Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.'''

import urllib.request

while True:
    host1 = input('Enter a url: ')
    
    count1 = 0
    try:
        fhand = urllib.request.urlopen(host1)
        for line in fhand:
            if count1 <= 3000:
                print(line.decode().strip())
                count1 = count1 + len(line)
                count2 = count1
            else:
                count2 = count2 + len(line)
        print(count1, count2)       
        break

    except:
        print("Enter a valid url")
        continue