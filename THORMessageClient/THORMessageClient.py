import requests
import sys
from Crypto.PublicKey import RSA 
from Crypto.Random import acquire_random_servers, get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


def send_message():
    # creating a socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Client Socket Created')

    while True:
        # connecting to listening server
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


if __name__ =="__main__"
    from sys import argv

    if len(argv) > 1
        port=str(argv[1])
    
    while(True):
        
        messageInput = input("message: ")
        message = requests.post(
            ("http://127.0.0.1:%s" %(port)),
            data={"message": messageInput}
        )
        print(message.status_code, message.reason)