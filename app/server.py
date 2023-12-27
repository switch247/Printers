from http.server import BaseHTTPRequestHandler, HTTPServer
import json

intercepted_data = []

def get_intercepted_data():
    return intercepted_data

class PrintRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        json_data = json.loads(post_data.decode('utf-8'))
        intercepted_data.append(json_data)
        print(json_data)
        self.send_response(200)
        self.end_headers()

def run_server(server_class=HTTPServer, handler_class=PrintRequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
