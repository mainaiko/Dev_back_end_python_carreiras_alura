def identificador_palavras_longas(texto):
    palavras = texto.split()
    palavras_longas = [palavra for palavra in palavras if len(palavra) > 10]
    return palavras_longas