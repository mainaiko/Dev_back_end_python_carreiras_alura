'''
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

    Pedra ganha de Tesoura (Pedra quebra Tesoura);
    Tesoura ganha de Papel (Tesoura corta Papel);
    Papel ganha de Pedra (Papel cobre Pedra);
    Se ambos escolherem a mesma opção, é um empate.
'''
import random

from embaralhador import pedra_papel_tesoura

while True:
    usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    if usuario not in ["pedra", "papel", "tesoura"]:
        print("Opção inválida. Por favor, escolha pedra, papel ou tesoura.")
        continue
    sistema = random.choice(["pedra", "papel", "tesoura"])
    print (f"O computador escolheu: {sistema}")

    resultado = pedra_papel_tesoura(usuario, sistema)
    print(resultado)
    
    if input("Deseja jogar novamente? (s/n): ").lower() != "s":
        break
