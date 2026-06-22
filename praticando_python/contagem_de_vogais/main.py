'''
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

'''

from contador import contador_vogais

texto_usuario = input("Digite um texto: ")
numero_vogais = contador_vogais(texto_usuario)

print(f"O texto: //'{texto_usuario}'// contém {numero_vogais} vogais.")
