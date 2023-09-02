import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_pai)

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