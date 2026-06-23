import os

def exibir_nome_do_programa():
    print ("🅂 🄰 🄱 🄾 🅁   🄴 🅇 🄿 🅁 🄴 🅂 🅂")

def exibir_menu(): # ctrl + ] indenta todo mundo
    # menu de opções para o usuário  
    print("""1. Cadastrar restaurante  
    2. Listar restaurantes
    3. Ativar restaurante
    4. Sair""")

def finalizar_app(): # função para finalizar o aplicativo e limpar o terminal
    os.system("clear")
    print ("Obrigado por usar o Sabor Express! Até a próxima!")

def escolher_opcao():
    # variavel que armazena a opção escolhida pelo usuário
    opcao_escolhida = int(input("Digite a opção desejada: "))
    # estrutura de controle de fluxo para tratar as opções escolhidas pelo usuário
    if opcao_escolhida == 1:
        print ("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print ("Listar restaurantes")
    elif opcao_escolhida == 3:
        print ("Ativar restaurante")
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == "_main_": # define o programa principal
    main()

