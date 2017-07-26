import threading
import time

from sender import Sender
from heartbeat import Heartbeat
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
		self.tSayHelloToSienge = threading.Timer(3, main.threadSayHelloToSienge)
		self.tSayHelloToSienge.daemon = True
		self.tSayHelloToSienge.start() 
		Heartbeat().pulse()


if __name__ == "__main__":
	
	main = Main()
	main.threadServer() 
	main.threadSendFilesToSienge()
	main.threadSayHelloToSienge()
	
	threadView = threading.Thread(target = loadView)
	threadView.start()