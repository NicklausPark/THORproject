from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import random, string
from sys import argv
import requests

class generate_rsa_keys():

    def generate_rsa_key1(self):
        print("Generating Public Key and Saving to a File")
        secret_size = 128
        self.secret_code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=secret_size)
            )
        print("Randomly using " + self.secret_code + " to generate public key")
        self.key_1 = RSA.generate(2048)
        encrypted_key = self.key_1.exportKey(passphrase=self.secret_code, pkcs=8, protection="scryptAndAES128-CBC", format="PEM")
        print(encrypted_key)
        pub = RSA.import_key(encrypted_key, passphrase=self.secret_code)
        prepare_pub = pub.publickey().exportKey(format="PEM")
        file_out = open("server1.pem", "wb")
        with file_out as f:
            f.write(prepare_pub)    
            print("Successfully wrote Pubkey to File")
            f.close()
            

        private_key = open("server1_priv.pem", "wb")
        with private_key as g:
            g.write(self.key_1.exportKey('PEM'))
            g.close()
            
        
    def generate_rsa_key2(self):
        print("Generating Public Key 2 and Saving to a File")
        secret_size = 128
        secret_code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=secret_size)
            )
        print("Randomly using " + secret_code + " to generate public key")
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
        pub = RSA.import_key(encrypted_key, passphrase=secret_code)
        prepare_pub = pub.publickey().exportKey()
        file_out = open("server2.pem", "w+")
        with file_out as f:
            f.write(prepare_pub.decode("utf-8"))    
            print("Successfully wrote Pubkey to File")
            f.close()
        
        print(prepare_pub.decode("utf-8"))
    
    def generate_rsa_key3(self):
        print("Generating Public Key 3 and Saving to a File")
        secret_size = 128
        secret_code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=secret_size)
            )
        print("Randomly using " + secret_code + " to generate public key")
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
        pub = RSA.import_key(encrypted_key, passphrase=secret_code)
        prepare_pub = pub.publickey().exportKey()
        file_out = open("server3.pem", "w+")
        with file_out as f:
            f.write(prepare_pub.decode("utf-8"))    
            print("Successfully wrote Pubkey to File")
        print(prepare_pub.decode("utf-8"))
    

    def encrypt_message1(self):
        print("encrypting message with RSA key 1")
        file_out = open("encrypted_data.bin", "wb")
        message = Input_message
        encoded_message = message.encode("utf-8")
        
        recipient_key = RSA.import_key(open("server1.pem").read())
        session_key = get_random_bytes(16)
        
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        decode_cipher = cipher_rsa.encrypt(session_key)
        decode_cipher_string = str(decode_cipher)
        #file_out.write(decode_cipher)
        print(decode_cipher_string)
        input("")
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        self.ciphertext, tag = cipher_aes.encrypt_and_digest(encoded_message)
        [ file_out.write(x) for x in (cipher_aes.nonce, tag, self.ciphertext) ]
        file_out.close()
        print("Successfully Encrypted Message")

    def send_rsa_data(self):
        print("sending encrypted message to server:1")
        
        port = input("to what port?: ")
        
        self.message = requests.post(
                ("http://127.0.0.1:%s" %(port)),
                data={ 
                    self.secret_code.encode("")
                
                
                
                }
                
            )
        print(self.message.status_code, self.message.reason)
    
    def decrypt_rsa(self):
        print("decrypting message...")
        file_in = open("encrypted_data.bin", "rb")
        private_key = RSA.import_key(open("server1_priv.pem", "rb").read())

        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
    
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        self.data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        print(self.data.decode("utf-8"))
        
        
        


if __name__ == "__main__":
    rsa = generate_rsa_keys()
    rsa.generate_rsa_key1()
    rsa.send_rsa_data()

