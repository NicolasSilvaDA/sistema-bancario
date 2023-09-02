
# Conexão com o banco de dados
# Verificar IDs já existentes

from random import randint, sample

def gerarID():
    novo_id = ''
    char_check = {}

    for loop in range(0, 5):
        num = str(randint(0, 9))
        letra = chr(randint(65, 90))

        if num in char_check:
            char_check[num] += 1

            if char_check[num] < 2:
                novo_id += num

        else:
            char_check[num] = 1
            novo_id += num

        if letra in char_check:
            char_check[letra] += 1
                    
            if char_check[letra] < 2:
                novo_id += letra

        else:
            char_check[letra] = 1
            novo_id += letra
        
    novo_id = ''.join(sample(novo_id, len(novo_id)))
    
    return novo_id

