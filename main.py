import threading
import datetime
import dateutil
import app

from app.sender import Sender
from app.heartbeat import Heartbeat
from app.server import initServer
from app.viewApp import loadView
from app.configuracao import Configuracao

class Main:

	def __init__(self):
		self.configuracao = Configuracao()
		self.configuracao.load()
		self.tSendFilesToSienge = None
		self.tSayHelloToSienge = None
		self.tServer = None

	def threadServer(self):
		self.tServer = threading.Thread(target = initServer)
		self.tServer.daemon = True
		self.tServer.start() 

	def threadSendFilesToSienge(self):
		self.tSendFilesToSienge = threading.Timer(int(self.configuracao.interval), main.threadSendFilesToSienge)
		self.tSendFilesToSienge.daemon = True
		self.tSendFilesToSienge.start() 
		
		if self.shouldSendFiles():
			print("sending")
			Sender().sendFilesToSienge()
		else:
			print("not")

	def threadSayHelloToSienge(self):
		self.tSayHelloToSienge = threading.Timer(1200, main.threadSayHelloToSienge)
		self.tSayHelloToSienge.daemon = True
		self.tSayHelloToSienge.start() 
		Heartbeat().pulse()

	def shouldSendFiles(self):
		now = datetime.datetime.now()
		startTime = now.replace(hour=int(self.configuracao.startTime), minute=0, second=0)
		endTime = now.replace(hour=int(self.configuracao.endTime), minute=59, second=59)

		if startTime.time() > endTime.time():
			endTime += datetime.timedelta(days=1)
			
		return now.time() >= startTime.time() and now.time() <= endTime.time()

if __name__ == '__main__':
	main = Main()
	main.threadServer() 
	main.threadSendFilesToSienge()
	main.threadSayHelloToSienge()
	
	threadView = threading.Thread(target = loadView)
	threadView.start()