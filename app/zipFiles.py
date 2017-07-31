import zipfile
import os
import app

from app.configuracao import Configuracao

class ZipFile(object):

	def __init__(self):
		self.fileZip = []
		self.paths = []
		self.configuracao = Configuracao()
		self.configuracao.load()
		

	def __zipdir(self, path, ziper):
		os.chdir(self.configuracao.path)
		for root, dirs, files in os.walk(path):
			for file in files:
				ziper.write(os.path.join(root, file))
				self.fileZip.append(file)
				self.paths.append(os.path.join(root, file))


	def createZip(self, zipName):
		ziper = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
		
		for path in self.configuracao.pagamento['paths']:
			self.__zipdir(path, ziper)
			
		for path in self.configuracao.cobranca['paths']:
			self.__zipdir(path, ziper)
		
		for path in self.configuracao.conciliacao['paths']:
			self.__zipdir(path, ziper)
		
		ziper.close()


	def getZipFile(self):
		return self.fileZip


	def getPaths(self):
		return self.paths