import http.server
import os

os.chdir('/Users/deeps/Documents/inqa-site')

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

http.server.test(HandlerClass=Handler, port=8765, bind='127.0.0.1')
