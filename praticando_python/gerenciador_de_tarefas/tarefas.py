def gerenciador_tarefas(tarefas):
    print("Bem-vindo ao Gerenciador de Tarefas!")

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            tarefas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada com sucesso!")
        elif escolha == "2":
            if tarefas:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif escolha == "3":
            if tarefas:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida com sucesso!")
                else:
                    print("Número de tarefa inválido.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif escolha == "4":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")