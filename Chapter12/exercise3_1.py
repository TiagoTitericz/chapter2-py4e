'''Exercise 3: Use urllib to replicate the previous exercise of retrieving
the document from a URL'''

import urllib.request

while True:
    host1 = input('Enter a url: ')
    
    try:
        fhand = urllib.request.urlopen(host1)
        for line in fhand:
            print(line.decode().strip())
        break

    except:
        print("Enter a valid url")
        continue