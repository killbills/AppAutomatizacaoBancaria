import requests
import logging
from configuracao import Configuracao

class Heartbeat(object):

	def __init__(self):
		self.configuracao = Configuracao()
		self.configuracao.load()

	def pulse(self):
		try:
			response = requests.post(self.configuracao.url_heartbeat, headers = self.createHeaders())
		except Exception as e:
			logging.error('Pulse: Não foi possível conectar ao servidor')
	
	def createHeaders(self):
		return {'Content-Type': 'multipart/form-data', 'Token': self.configuracao.token}