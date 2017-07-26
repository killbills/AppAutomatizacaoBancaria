import requests
import time
import os
import shutil
import logging

from configuracao import Configuracao
from zipFiles import ZipFile
from historicoProcessamento import HistoricoProcessamento

class Sender(object):

	def __init__(self):
		logging.info(' Enviando arquivos para o SIENGE...')
		self.configuracao = Configuracao()
		self.configuracao.load()
		self.ziper = ZipFile()


	def sendFilesToSienge(self):
		zipName = "arquivosAutomatizacaoBancaria.zip"

		self.ziper.createZip(zipName)

		header = self.createHeader()
		zipFile = open(zipName, 'rb').read()
		response = None

		try:
			response = requests.post(self.configuracao.url, headers = header, timeout = 60, data = zipFile)
		except Exception as e:
			logging.error(' Não foi possível conectar ao servidor')


		statusCode = self.createHistoricoProcessamento(response)

		if statusCode == 200:
			self.moveFiles()


		os.remove(os.path.join(zipName))


	def createHeader(self):
		return {'Content-Type': 'multipart/form-data', 'Token': self.configuracao.token}


	def createHistoricoProcessamento(self, response):

		execucao = HistoricoProcessamento().Execucao()

		if response != None:
			execucao.status = response.status_code

			if response.status_code == 200:
				execucao.mensagem = "Sucesso"
			if response.status_code == 500:
				execucao.mensagem = "Falha no servidor"
			if response.status_code == 401:
				execucao.mensagem = "Token nao autorizado"

		else:
			execucao.mensagem = "Não foi possível conectar ao servidor"
			execucao.status = ""
			
		
		execucao.totalArquivos = len(self.ziper.getZipFile())
		execucao.paths = self.ziper.getPaths()
		execucao.data = time.strftime('%d/%m/%Y - %H:%M:%S')
		
		for fileZip in self.ziper.getZipFile():
			execucao.arquivos.append(fileZip.encode("utf-8"))
		
		
		historicoProcessamento = HistoricoProcessamento()
		historicoProcessamento.carregar()

		historicoProcessamento.execucao.append(execucao)
		historicoProcessamento.salvar()

		return execucao.status


	def moveFiles(self):
		for source in self.ziper.getPaths():
			
			dest = os.path.join("Processados", source)
			logging.info(' Movendo arquivos...')
			localPath = dest.rsplit('\\', 1)[0]
			os.makedirs(localPath, 0o777, True)
			
			if os.path.isfile(dest):
				os.chmod(dest, 0o777)
				os.remove(dest)
				
			
			shutil.move(source, dest)	