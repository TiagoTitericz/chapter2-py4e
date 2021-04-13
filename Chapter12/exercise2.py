'''Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire document and count the total 
number of characters and display the count
of the number of characters at the end of the document.'''

import socket

while True:
    host1 = input('Enter a url: ')
    host2 = host1.split('/')

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mysock.connect((host2[2], 80))
        cmd = (f'GET {host1} HTTP/1.0\r\n\r\n').encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(5120)
            if len(data) < 1:
                break
            print(data[0:3000].decode(),end='')
            print('The entire document length:', len(data))
            if len(data) < 3000:
                print(f'{len(data)} caracters printed out')
            else:
                print('3000 caracters printed out')
        break

    except:
        print("Enter a valid url")
        continue

mysock.close()
