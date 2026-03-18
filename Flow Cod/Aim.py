import http.server
import socketserver
import threading
import webbrowser

PORT = 6545

def start_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

# Run server in background
thread = threading.Thread(target=start_server, daemon=True)
thread.start()

# Open browser
webbrowser.open(f"http://localhost:{PORT}")

# Keep script alive
input("Press Enter to stop server...\n")
