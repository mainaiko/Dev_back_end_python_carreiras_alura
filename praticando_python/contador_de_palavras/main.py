from contador import contar_palavras

frase = input('Digite uma frase: ').strip() # verifica se a entrada esta vazia


if not frase:
    print("Erro: Por favor, digite uma frase válida.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print (f'A frase digitada foi: {frase}')
        print ('contagem de palabras: ')
        for palavra, frequencia in resultado.items():
            print(f'{palavra}: {frequencia}')
    else:
        print(f'A frase "{frase}" não contém palavras válidas para contar.')