def contador_vogais(texto):
    vogais = 'AEIOUaeiou'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador
