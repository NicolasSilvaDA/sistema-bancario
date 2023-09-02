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

def cadastro_cliente(connection, cpf, nome, telefone):

    query = f"""
    insert into cliente values(
    '{cpf}', '{nome}', '{telefone}'
    );
    """

    executar_query(connection, query)

def cadastro_conta(connection, id, num_conta, cliente, saldo=0.0):

    query = f"""
    insert into conta values(
    '{id}', {saldo}, '{num_conta}', '{cliente}'
    );
    """

    executar_query(connection, query)


connection = criar_conexao_bd("localhost",
                               input("Usuário: "),
                               getpass("Senha: "),
                               "sistemabancario")


# cliente_table = """
# """
# executar_query(connection, cliente_table)

# cadastro_cliente(connection, "12345678911", "Geraldo Luiz", "81998765432")
# cadastro_conta(connection, '1XSK2F56J9', '0025456781', '12345678911')
