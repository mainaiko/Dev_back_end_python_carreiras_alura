import re

def calculo_gorjeta(valor_conta, percentual_gorjeta): # funcao para calcular o valor da gorjeta e o valor total a ser pago
    valor_gorjeta = valor_conta * (percentual_gorjeta / 100)
    valor_total = valor_conta + valor_gorjeta
    return valor_gorjeta, valor_total

def manter_apenas_numeros(texto): # funcao para manter apenas os numeros da string de entrada, removendo qualquer caractere que nao seja numero
    if texto is None:
        return ""
    else:
        return re.sub(r'[^0-9]', '', texto)
    
