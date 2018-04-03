import socket
import sys
from Crypto.Cipher import SHA256
from Crypto.Random import acquire_random_servers
 

def encrypt( self, raw ):
    
    raw = SHA256.new()
    encrypt = hash.update(input('What is your message?'))
    
#key = random_bytes(16)
#cipher = AES.new(key, AES.MODE_EAX)
#ciphertext, tag = cipher.encrypt and digest(data)
#    pass

def send_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Client Socket Created')

    while True:
        s.connect(('localhost', 8888))
        print ('Connecting to the server...')
        hosts = acquire_random_servers()
    
        try:
            while True:
                message2 = str.encode(message)
                s.sendall(message2)
            if message:
                print ('Sending your message of ' + message)
            else:
                break
        finally:
            s.close()


