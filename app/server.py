import logging
import time
import os
import app

from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		message = "Hello world!"
		self.wfile.write(bytes(message, "utf8"))
		return


def initServer():
	os.makedirs(os.path.join(os.path.dirname(__file__), 'logs'), 0o777, True)
	path=os.path.join(os.path.dirname(__file__), 'logs\\console.log')
	logging.basicConfig(filename=path, level=logging.INFO)
	logging.info(' Starting service - ' + time.strftime('%c'))
	server_address = ('127.0.0.1', 9095)
	httpd = HTTPServer(server_address, Server)
	httpd.serve_forever()