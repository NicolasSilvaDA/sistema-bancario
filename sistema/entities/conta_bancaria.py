import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_pai)

# O código acima tem a função de reconhecer o diretório pai como caminho absoluto
# do projeto, evitando erros de reconhecimento de diretório ao importar outros
# módulos.

from funcoes_gerais import *

class ContaBancaria:
    def __init__(self, saldo=0.0):
        self.num_conta = gerar_num_conta()
        self.saldo = saldo
