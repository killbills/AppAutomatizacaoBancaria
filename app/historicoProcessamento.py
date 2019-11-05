import os
import json
import jsonpickle
import time
import app

from pathlib import Path

caminhoArquivo = os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/docs/historicoEnvio_'+time.strftime('%d_%m_%Y')+'.json')

class HistoricoProcessamento:

    def __init__(self):
        self.execucao = []


    class Execucao():
        def __init__(self):
            self.status = None
            self.mensagem = None
            self.data = None
            self.totalArquivos = None
            self.arquivos = []
            self.paths = []


    def carregar(self):
        
        historicoFile = Path(caminhoArquivo)
        if not historicoFile.is_file():
            with open(caminhoArquivo, 'w') as f:
                f.write(jsonpickle.encode(self.__dict__))

        with open(caminhoArquivo, 'r') as file:
            self.__dict__ = json.load(file)


    def salvar(self):            
        with open(caminhoArquivo, 'w') as file:
            file.write(jsonpickle.encode(self.__dict__))