import http.server
import os
import sys

os.chdir("/Users/bradstricker/Documents/Claude/Projects/Institutional IA")
handler = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer(("", 8000), handler)
print("Serving on http://localhost:8000")
sys.stdout.flush()
server.serve_forever()
