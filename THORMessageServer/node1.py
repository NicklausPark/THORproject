import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8888))
s.listen(1)

conn, addr = s.accept()
while 1:
    data = conn.recv(4080).decode('ascii')
    if not data:
        break
    conn.sendall(data).encode
conn.close()

socket.send('Hello World\n')
socket.close()





