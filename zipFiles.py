import zipfile
import os

from configuracao import Configuracao

class ZipFile(object):

	def __init__(self):
		self.fileZip = []
		self.paths = []
		

	def zipdir(self, path, ziper):
		for root, dirs, files in os.walk(path):
			for file in files:
				ziper.write(os.path.join(root, file))
				self.fileZip.append(file)
				self.paths.append(os.path.join(root, file))


	def createZip(self, zipName):
		ziper = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
		
		configuracao = Configuracao()
		configuracao.load()
		
		for path in configuracao.pagamento['paths']:
			self.zipdir(path, ziper)
			
		for path in configuracao.cobranca['paths']:
			self.zipdir(path, ziper)
		
		for path in configuracao.conciliacao['paths']:
			self.zipdir(path, ziper)
		
		ziper.close()


	def getZipFile(self):
		return self.fileZip


	def getPaths(self):
		return self.paths