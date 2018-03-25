from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import sys

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (sys.argv[1], int(sys.argv[2]))
    httpd = server_class(server_address, handler_class)
    print("Successfully started server at", server_address)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

