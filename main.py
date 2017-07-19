import threading
import time

from sendFilesToSienge import Sender
from sayHelloToSienge import sayHelloToSienge
from server import initServer
from viewApp import loadView


class Main:

	def __init__(self):
		self.tSendFilesToSienge = None
		self.tSayHelloToSienge = None
		self.tServer = None


	def threadServer(self):
		self.tServer = threading.Thread(target = initServer)
		self.tServer.daemon = True
		self.tServer.start() 


	def threadSendFilesToSienge(self):
		self.tSendFilesToSienge = threading.Timer(180, main.threadSendFilesToSienge)
		self.tSendFilesToSienge.daemon = True
		self.tSendFilesToSienge.start() 
		Sender().sendFilesToSienge()



	def threadSayHelloToSienge(self):
		self.tSayHelloToSienge = threading.Timer(1200, main.threadSayHelloToSienge)
		self.tSayHelloToSienge.daemon = True
		self.tSayHelloToSienge.start() 
		sayHelloToSienge()


if __name__ == "__main__":
	
	main = Main()
	main.threadServer() 
	main.threadSendFilesToSienge()
	main.threadSayHelloToSienge()
	
	threadView = threading.Thread(target = loadView)
	threadView.start()