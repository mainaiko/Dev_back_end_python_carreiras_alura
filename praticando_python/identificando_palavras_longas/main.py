'''
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.
'''
from identificador import identificador_palavras_longas


texto_usuario = input("Digite um texto: ")
palavras_longas = identificador_palavras_longas(texto_usuario)

print (f"As palavras longas encontradas no texto são: {palavras_longas}") if palavras_longas else print("Nenhuma palavra longa encontrada no texto.")
