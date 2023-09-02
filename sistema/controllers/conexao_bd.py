"""
    Este módulo é responsável por estabelecer e gerenciar todas
    as operações referentes ao banco de dados   
"""

# MySQL <-> Python
import mysql.connector
from mysql.connector import Error
# import pandas as pd 

# Tratamento de senha
from getpass import getpass

# Conexão com o banco de dados
def criar_conexao_bd(host, usuario, senha, bd):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=usuario,
            passwd=senha,
            database=bd
        )

        print("Conexão com o banco de dados bem-sucedida!")
    except Error as err:
        print(f'Erro: "{err}"')
    
    return connection

def executar_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query realizada com sucesso!")
    except Error as err:
        print(f'Erro: "{err}"')

def executar_fetch(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    except Error as err:
        print(f'Erro: "{err}"')


# connection = criar_conexao_bd("localhost",
#                                input("Usuário: "),
#                                getpass("Senha: "),
#                                "sistemabancario")
