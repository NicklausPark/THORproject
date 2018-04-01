import socket
import sys

HOST = 'localhost'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print("Bind failed. Error Code : " + str(msg[0]))
    sys.exit()

print('Socket bind Complete')

s.listen(10)
print ('Socket now listening')

while True:
    conn, addr = s.accept()
    try:
        while True:
            data = conn.recv(4096).decode('ascii')
            if data:
                print(data) 
            else:
                break
    finally:
        s.close()
