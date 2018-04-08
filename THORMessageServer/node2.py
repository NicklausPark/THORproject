import socket
import sys
from Crypto.PublicKey import RSA 
from Crypto.Random import acquire_random_servers, get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP



    def generate_rsa_key_2():
        secret_code = "keyforserver2"
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=secret_code, pksc=8, protection="scryptAndAES128-CBC")
        file_out = open("server2.pem")
    
    