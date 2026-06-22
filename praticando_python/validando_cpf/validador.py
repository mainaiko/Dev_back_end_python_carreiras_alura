import re

def validador_cpf(cpf):
    cpf_limpo = re.sub(r'[^0-9]', '', cpf)  # Remove caracteres não numéricos

    if len(cpf_limpo) != 11:
        return False # Retorna False se o CPF não tiver exatamente 11 dígitos
    
    if cpf_limpo == cpf_limpo[0] * 11:
        return False # Retorna False se todos os dígitos forem iguais
    
    # Calcula a soma dos primeiros 9 dígitos multiplicados pelos pesos correspondentes
    soma_1 = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9)) # i = index, 10 - i = peso ou seja o python executa primeiro o for atribuindo i ao range 0 e apos isso usa o i para resolver os parenteses e depois multiplica o resultado quando o python termina os 9 resultados sao somados
    digito_1 = (soma_1 * 10) % 11 # o resultado da soma é multiplicado por 10 depois uma divisao inteirra por 11 e o resto dessa divisao é o digito verificador, se o resultado for 10 o digito verificador é 0
    digito_1 = 0 if digito_1 == 10 else digito_1

    if digito_1 != int(cpf_limpo[9]):
        return False # Retorna False se o primeiro dígito verificador não for válido
    
    # Calcula a soma dos 10 dígitos multiplicados pelos pesos correspondentes
    soma_2 = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
    digito_2 = (soma_2 * 10) % 11
    digito_2 = 0 if digito_2 == 10 else digito_2

    if digito_2 != int(cpf_limpo[10]):
        return False # Retorna False se o segundo dígito verificador não for válido
    
    return True

    