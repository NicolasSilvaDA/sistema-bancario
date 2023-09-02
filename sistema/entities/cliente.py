import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_pai)

# O código acima tem a função de reconhecer o diretório pai como caminho absoluto
# do projeto, evitando erros de reconhecimento de diretório ao importar outros
# módulos.

from funcoes_gerais import *

class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        self._id = gerarID()

        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @property
    def id(self):
        # Verificar permissões
        return self._id
    
geraldo = Cliente("Geraldo Luiz", "12345678911", "81987654321")

print(geraldo.id)