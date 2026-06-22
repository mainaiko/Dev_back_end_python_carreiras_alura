def jogo_advinha():
    import random

    numero_aleatorio = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            if palpite < 1 or palpite > 100:
                raise ValueError("Número fora do intervalo permitido.")
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
            continue

        tentativas += 1

        if palpite < numero_aleatorio:
            print("O número é maior. Tente novamente.")
        elif palpite > numero_aleatorio:
            print("O número é menor. Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
            break
