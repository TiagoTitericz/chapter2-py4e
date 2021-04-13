'''Exercise 1: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.'''

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
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end='')
        break

    except:
        print("Enter a valid url")
        continue

mysock.close()
