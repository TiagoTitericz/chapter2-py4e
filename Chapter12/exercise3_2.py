'''Exercise 3: Use urllib to replicate the previous exercise of retrieving
the document from a URL, displaying up to 3000 characters'''

import urllib.request

while True:
    host1 = input('Enter a url: ')
    
    count = 0
    try:
        fhand = urllib.request.urlopen(host1)
        for line in fhand:
            if count <= 3000:
                print(line.decode().strip())
                count = count + len(line)
        break

    except:
        print("Enter a valid url")
        continue