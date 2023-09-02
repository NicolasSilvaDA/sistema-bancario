import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_pai)

# O código acima tem a função de reconhecer o diretório pai como caminho absoluto
# do projeto, evitando erros de reconhecimento de diretório ao importar outros
# módulos.

from controllers import *

from mysql.connector import Error
from getpass import getpass

def cadastro_cliente(connection, cpf, nome, telefone):

    query = f"""
    INSERT INTO cliente VALUES(
    '{cpf}', '{nome}', '{telefone}'
    );
    """

    executar_query(connection, query)


def consulta_cliente(connection, cpf):
    try:
        query = f"""
        SELECT * FROM cliente
        WHERE cpf={cpf};
        """

        cliente = {}
        result = executar_fetch(connection, query)
        
        if result != None:
            itens = []
            for item in result[0]:
                itens.append(item)
            
            cliente = {
                "cpf" : itens[0],
                "nome" : itens[1],
                "telefone" : itens[2]
            }

        return cliente

    except Error as err: # Tratamento de erros básico para teste
        print(f"Não foi possível realizar sua solicitação! Erro: '{err}'")

# connection = criar_conexao_bd(
#     'localhost',
#     input("Usuário: "),
#     getpass("Senha: "),
#     'sistemabancario'
# )

# print(consulta_cliente(connection, '12345678911'))
