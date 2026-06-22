# minha tentativa

'''
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.


passo 1 = entrada e processamento de dados
passo 2 = calcular a gorjeta
passo 3 = exibir o resultado para o usuário
passo 4 = testar e refinar o codigo

regras de negocio:
valor da conta = deve ser um numero positivo
porcentagem de gorjeta = deve ser um numero positivo
valor da gorjeta = deve ser calculado corretamente com base no valor da conta e na porcentagem de gorjeta
total a ser pago = deve ser a soma do valor da conta e do valor da gorjeta
entrada invalida = o codigo deve tratar entradas invalidas e solicitar ao usuario que digite novamente
'''
from calcular_gorjeta import calculo_gorjeta, manter_apenas_numeros

try:
    valor_conta = float(input("Digite o valor total da conta: "))
    percentual_gorjeta = input("Digite a porcentagem de gorjeta desejada: ") #input nunca retorna None somente string vazia
    
    str_limpa = manter_apenas_numeros(percentual_gorjeta) # convertendo a string de entrada para apenas numeros

    if valor_conta > 0: # verificando se o valor da conta é positivo
        if str_limpa == "": # se o usuario nao digitar nada ou digitar algo que nao seja numero, a gorjeta padrao sera de 10%
            percentual_gorjeta = 10.0
        else: # se o usuario digitar um valor valido, a gorjeta sera calculada com base nesse valor
            percentual_gorjeta = float(str_limpa)

        valor_gorjeta, valor_total = calculo_gorjeta(valor_conta, percentual_gorjeta) # instanciando a funcao de calculo_gorjeta
        print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
        print(f"Total a ser pago: R$ {valor_total:.2f}")
    else: # se o valor da conta for negativo ou zero, o programa exibira uma mensagem de erro
        print("Valor da conta deve ser um número positivo.")

except ValueError: # se o usuario digitar algo que nao seja um numero, o programa exibira uma mensagem de erro
    print("Erro: Por favor, digite apenas números válidos.")
except Exception as e: # para capturar qualquer outro tipo de erro inesperado e exibir uma mensagem de erro genérica
    print(f"Ocorreu um erro inesperado: {e}")


