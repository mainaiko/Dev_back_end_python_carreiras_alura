# primeiro_numero = float(input("Digite o primeiro número: "))
# segundo_numero = float(input("Digite o segundo número: "))

# soma = primeiro_numero + segundo_numero // soma nao esta encapsulada em uma funcao e poderia ser melhor

def somar_numeros(num1, num2):  #funcao encapsula a soma de dois numeros
    return num1 + num2

# chamada_func_somar = somar_numeros(primeiro_numero, segundo_numero) // variavel que armazena o retorno da funcao somar_numeros


# print(f"A soma de {primeiro_numero} e {segundo_numero} é: {chamada_func_somar}") // caso o usuario digite algo errado tenho que tratar o erro

try:
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    chamada_func_somar = somar_numeros(primeiro_numero, segundo_numero)
    print(f"A soma de {primeiro_numero} e {segundo_numero} é: {chamada_func_somar}")


except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")

'''
entrada invalida = ValueError
tipo invalido = TypeError
indice fora do alcance = IndexError
chave nao encontrada = KeyError
erro de importacao = ImportError
modulo nao encontrado = ModuleNotFoundError
atributo nao encontrado = AttributeError
sintaxe invalida = SyntaxError
nome nao definido = NameError
'''

# para conhecer mais sobre erros especificos consulte a ducumentação oficial do python
# conheça a pep8 para padronizar seu codigo e facilitar a leitura de outros programadores





