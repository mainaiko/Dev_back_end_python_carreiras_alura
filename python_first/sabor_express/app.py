import os

print ("🅂 🄰 🄱 🄾 🅁   🄴 🅇 🄿 🅁 🄴 🅂 🅂")

# menu de opções para o usuário
print("""1. Cadastrar restaurante
2. Listar restaurantes
3. Ativar restaurante
4. Sair""")

# variavel que armazena a opção escolhida pelo usuário
opcao_escolhida = int(input("Digite a opção desejada: "))

# print (f"voce escolheu a opção: {opcao_escolhida}")

# função para finalizar o aplicativo e limpar o terminal
def finalizar_app():
    os.system("clear")
    print ("Obrigado por usar o Sabor Express! Até a próxima!")

# estrutura de controle de fluxo para tratar as opções escolhidas pelo usuário
if opcao_escolhida == 1:
    print ("Cadastrar restaurante")
elif opcao_escolhida == 2:
    print ("Listar restaurantes")
elif opcao_escolhida == 3:
    print ("Ativar restaurante")
else:
    finalizar_app()

