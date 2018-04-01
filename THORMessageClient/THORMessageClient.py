import socket
import sys

HOST = 'localhost'
PORT = 8887

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Client Socket Created')

while True:
    s.connect(('localhost', 8888))
    print ('Connecting to the server...')
    
    try:
        while True:
            message = input('What is your message? ')
            message2 = str.encode(message)
            s.sendall(message2)
        if message:
            print ('Sending your message of ' + message)
        else:
            break
    finally:
        s.close()