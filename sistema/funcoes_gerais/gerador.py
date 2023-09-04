
# Conexão com o banco de dados
# Verificar IDs já existentes

from random import randint, sample


def gerar_num_conta():
    num_conta = str(randint(10000000, 99999999))
    digito_calc = 0
    divisor = 9

    for num in num_conta:
        digito_calc += int(num) * divisor
        divisor -= 1
    
    digito_calc %= 11

    digito_calc = 'X' if digito_calc == 10 else str(digito_calc)

    num_conta += '-' + digito_calc

    return num_conta

# def gerar_id():
#     novo_id = ''
#     char_check = {}

#     while len(novo_id) < 10:
#         num = str(randint(0, 9))
#         letra = str(randint(65, 90))

#         if num in char_check:
#             if char_check[num] < 2:
#                 novo_id += num
            
#             char_check[num] += 1

#         else:
#             char_check[num] = 1
#             novo_id += num

#         if letra in char_check:
#             char_check[letra] += 1
                    
#             if char_check[letra] < 2:
#                 novo_id += letra

#         else:
#             char_check[letra] = 1
#             novo_id += letra
        
#     novo_id = ''.join(sample(novo_id, len(novo_id)))
    
#     return novo_id