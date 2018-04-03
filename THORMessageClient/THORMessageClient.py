import socket
import sys
from Crypto.PublicKey import RSA 
from Crypto.Random import acquire_random_servers, get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP



# these functions will generate 3 different RSA keys and store them into files with a secret passphrase

class generate_rsa_keys():

    def generate_rsa_key_1():
        secret_code = "keyforserver1"
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
        file_out = open("server1.pem")

    def generate_rsa_key_2():
        secret_code = "keyforserver2"
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=secret_code, pksc=8, protection="scryptAndAES128-CBC")
        file_out = open("server2.pem")

    def generate_rsa_key_3():
        secret_code = "keyforserver3"
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
        file_out = open("sever3.pem")

# these functions will encrypt the data with the 3 different 


def encrypt_data_key_1( self, raw ):
    file_out = open("encrypted_data.bin", "wb")
    recipient_key = RSA.import_key(open("server1.pem").read())
    session_key = get_random_bytes(16)

def encrypt_data_key_2( self, raw ):
    file_out = open()
    


    
    
#key = random_bytes(16)
#cipher = AES.new(key, AES.MODE_EAX)
#ciphertext, tag = cipher.encrypt and digest(data)
#    pass

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


