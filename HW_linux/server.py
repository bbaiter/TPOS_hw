import argparse

from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"GET {self.path}\n", flush=True)
        body = "OK\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

parser = argparse.ArgumentParser()
parser.add_argument("--port",type=int, required=True)
args = parser.parse_args()

server = HTTPServer(("127.0.0.1",args.port),Handler)
print(f"Server running at http://127.0.0.1:{args.port}", flush=True)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped", flush=True)
finally:
    server.server_close()