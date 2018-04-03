import socket
import sys

HOST = 'localhost'
PORT = 8888

# creating a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')

# binding to a port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print("Bind failed. Error Code : " + str(msg[0]))
    sys.exit()

print('Socket bind Complete')

# socket is listening with 10 connection queue
s.listen(10)
print ('Socket now listening')

# socket accepts data while in a while true loop
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
