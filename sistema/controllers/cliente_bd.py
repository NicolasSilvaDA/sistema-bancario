import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_pai)

# O código acima tem a função de reconhecer o diretório pai como caminho absoluto
# do projeto, evitando erros de reconhecimento de diretório ao importar outros
# módulos.

from controllers import conexaoBD

def cadastro_cliente(cpf, nome, telefone):

    query = f"""
    INSERT INTO cliente VALUES(
    '{cpf}', '{nome}', '{telefone}'
    );
    """

    conexaoBD.executar_query(query)


def consulta_cliente(cpf):
    query = f"""
    SELECT * FROM cliente
    WHERE cpf='{cpf}';
    """

    cliente = {}
    result = conexaoBD.executar_fetch(query)
        
    if result:
        itens = [item for item in result[0]]
            
        cliente = {
            "cpf" : itens[0],
            "nome" : itens[1],
            "telefone" : itens[2]
        }
    else:
        print("Nenhum cliente foi encontrado!")


    return cliente


# consulta_cliente('98765432111')