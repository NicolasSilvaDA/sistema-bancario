import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_pai)

# O código acima tem a função de reconhecer o diretório pai como caminho absoluto
# do projeto, evitando erros de reconhecimento de diretório ao importar outros
# módulos.

from controllers import conexaoBD
from entities import ContaBancaria

def cadastro_conta(num_conta, cliente, saldo=0.0):

    query = f"""
    INSERT INTO conta VALUES(
    '{num_conta}', {saldo}, '{cliente}'
    );
    """

    conexaoBD.executar_query(query)

def consulta_conta(num_conta):

    query = f"""
    SELECT * FROM conta
    WHERE num_conta='{num_conta}';
    """

    dados_bancarios = {}
    result = conexaoBD.executar_fetch(query)

    if result:
        dados = [item for item in result[0]]

        dados_bancarios = {
            "num_conta" : dados[0],
            "saldo" : dados[1],
            "cliente" : dados[2]
        }

    else:
        print("Nenhuma conta foi encontrada!")
    
    return dados_bancarios
