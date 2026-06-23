'''
Exercícios

1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

    Criança: 0 a 12 anos;
    Adolescente: 13 a 18 anos;
    Adulto: acima de 18 anos.

3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

    Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    Caso contrário: o ponto está localizado no eixo ou origem.
'''


# exercicio numero 1

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")

# exercicio numero 2

digite_sua_idade = int(input("Digite sua idade: "))

if digite_sua_idade <= 12:
    print("Criança")
elif digite_sua_idade <= 18:
    print("Adolescente")
else:
    print("Adulto")

# exercicio numero 3

nome_de_usuario = str(input("Digite seu nome de usuario: "))
senha = str(input("Digite sua senha: "))

if nome_de_usuario == "lorins" and senha == "12345":
    print ("Usuario e senha corretos")
else:
    print ("Usuario e senha incorretos")

# exercicio numero 4

coordenada_x = int(input("Digite a coordenada x: "))
coordenada_y = int(input("Digite a coordenada y: "))

if coordenada_x > 0 and coordenada_y > 0:
    print("Primeiro Quadrante")
elif coordenada_x < 0 and coordenada_y > 0:
    print("Segundo Quadrante")
elif coordenada_x < 0 and coordenada_y < 0:
    print("Terceiro Quadrante")
elif coordenada_x > 0 and coordenada_y < 0:
    print("Quarto Quadrante")
else:
    print("O ponto está localizado no eixo ou na origem")