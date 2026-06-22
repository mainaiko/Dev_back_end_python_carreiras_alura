def contar_palavras(frase):
    frase = limpar_texto(frase) # limpa o texto para evitar contagem incorreta
    if not frase.strip():
        return {}
    palavras = frase.split()  # Divide a frase em palavras usando o espaço como separador
    contagem = {}
    for palavra in palavras:
            contagem[palavra] = contagem.get(palavra, 0) + 1 # incrementa a contagem da palavra
    return contagem
    # print (palavras) # exibe a lista de palavras para o usuário
    # return len(palavras)  # Retorna o número de palavras

def limpar_texto(texto):
    texto = texto.lower() # converte o texto para minusculo
    caracteres_especiais = "!@#$%^&*()_+-=~`[]{}|;:'\",.<>?/\\" # lista de caracteres especiais a serem removidos
    for char in caracteres_especiais: # percorre a lista de caracteres especiais
        texto = texto.replace(char, "") # remove os caracteres especiais do texto e substitui por vazio
    return texto


