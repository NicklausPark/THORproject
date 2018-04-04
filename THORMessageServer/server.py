from BaseHTTPServer import BaseHTTPServer, HTTPServer
import urlib.parse
import requests
import sys
from Crypto.PublicKey import RSA 
from Crypto.Random import acquire_random_servers, get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

class node(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = urllib.parse.unquote_plus(post_data)
        self._set_headers()
        print(post_data)

    
def run (server_class=HTTPServer, handler_class=Node, port=4224):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting HTTP Server on port", port)
    httpd.serve_forever()        

if __name__ = "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1])
    else:
        run()
        
