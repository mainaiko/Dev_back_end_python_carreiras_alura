'''
Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

    Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
    Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.
'''
from calculadora import calculadora

while True:
    try:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        operacao = input("Escolha a operação (soma, subtracao, multiplicacao, divisao): ").lower()

        resultado = calculadora(valor1, valor2, operacao)
        print(f"O resultado da {operacao} entre {valor1} e {valor2} é: {resultado}")
        if input("Deseja realizar outra operação? (s/n): ").lower() != 's':
            break

    except ValueError as ve:
        print(f"Erro de valor: {ve}. Tente novamente.")
    except ZeroDivisionError as zde:
        print(f"Erro de divisão: {zde}. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")