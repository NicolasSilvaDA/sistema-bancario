from controllers import *

def cadastro_conta(connection, id, num_conta, cliente, saldo=0.0):

    query = f"""
    insert into conta values(
    '{id}', {saldo}, '{num_conta}', '{cliente}'
    );
    """

    executar_query(connection, query)
