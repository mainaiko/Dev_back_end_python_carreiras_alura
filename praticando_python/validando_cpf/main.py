'''
Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

'''
from validador import validador_cpf

cpf_cliente = input("Digite o CPF do cliente (somente números): ")

if validador_cpf(cpf_cliente):
    print("CPF válido!")
else:
    print("CPF inválido. Certifique-se de que o CPF contém exatamente 11 dígitos numéricos e não possui caracteres inválidos.")


