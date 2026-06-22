# minha tentativa 

def contar_palavras(frase):
    palavras = frase.split()  # Divide a frase em palavras usando o espaço como separador
    return len(palavras)  # Retorna o número de palavras

# try e except para tratar possíveis erros na entrada do usuário
try:
    frase_usuario = input('Digite uma frase: ')
    numero_palavras = contar_palavras(frase_usuario)
    print(f'A frase "{frase_usuario}" contém {numero_palavras} palavras.')

except ValueError:
    print("Erro: Por favor, digite uma frase válida.")

# resposta professor alura

'''
problema geral = contar palavras em uma frase
passo 1 = entrada e processamento de dados
passo 2 = criar a contagem de palavras
passo 3 = exibir o resultado para o usuário
passo 4 = testar e refinar o codigo

criar uma função para contar palavras em uma frase e coloque em um arquivo separado para que possa ser reutilizada em outros programas
criar um arquivo main para testar a função criada e exibir o resultado para o usuário

regras de negocio:
entrada vazia = o codigo pode falhar
apenas espaços = deve ser considerado vazio
apenas pontuação = map contem palavras validas
texto com pontuação = a pontuação deve ser ignorada e as palavras devem ser contadas normalmente
caracteres especiais = podem gerar contagem incorreta caso nao haja tratamento adequado
varios espaços entre palavras = deve ser tratado para evitar contagem incorreta
palavras repetidas = devem contar corretamente a frequencia
maiusculas e minusculas = devem ser tratadas como iguais
numeros na frase = devem ser contados como palavras
somente numeros = devem ser contados como palavras
mistura de letras e numeros = a pontuação pode separar indevidamente
'''






