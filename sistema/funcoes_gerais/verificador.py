def verificar_cpf(cpf):
    nove_digitos = cpf[0:9]
    prim_dv = cpf[9]
    seg_dv = cpf[10]

    # Cálculo para o primeiro dígito
    soma = 0
    count = 10

    for digito in nove_digitos:
        soma += int(digito) * count
        count -= 1

    soma *= 10

    resto = 0 if soma % 11 > 9 else soma % 11
    
    if resto != int(prim_dv):
        return False
    
    # Cálculo para o segundo dígito
    soma = 0
    count = 11
    dez_digitos = nove_digitos + prim_dv

    for digito in dez_digitos:
        soma += int(digito) * count
        count -= 1
    
    soma *= 10
    
    resto = 0 if soma % 11 > 9 else soma % 11

    if resto != int(seg_dv):
        return False

    return True

