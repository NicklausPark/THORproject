from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP
import random, string


class generate_rsa_keys():

    def generate_rsa_key1(self):
        secret_size = 128
        secret_code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=secret_size)
            )
        print(secret_code)
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
        pub = RSA.import_key(encrypted_key, passphrase=secret_code)
        prepare_pub = pub.publickey().exportKey()
        file_out = open("server1.pem", "w+")
        print("Generating Public Key and Saving to a File")
        with file_out as f:
            f.write(prepare_pub.decode("utf-8"))    



if __name__ == "__main__":
    rsa = generate_rsa_keys()
    rsa.generate_rsa_key1()

