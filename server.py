import json
from http.client import responses
import socketserver

from http.server import SimpleHTTPRequestHandler, HTTPServer
import cgi

PORT = 8000
class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print(post_data.decode('utf-8'))
        #response = f"Received POST data: {post_data.decode('utf-8')}"
        response = str(type(json.loads(
            post_data.decode('utf-8')
        )["y"]))
        self.wfile.write(response.encode('utf-8'))

httpd =  socketserver.TCPServer(("0.0.0.0", PORT), MyHandler)

print("Starting server on port 8000...")
httpd.serve_forever()