from BaseHTTPServer import BaseHTTPRequestHandler, BaseHTTPServer, CGIHTTPRequestHandler 
import socketserver

class THORclass(BaseHTTPRequestHandle):

    def _set_headers(self): 
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        