def menu():
    while True:
        print("\n--- MENU ESCOLA ---")
        print("1. Cadastrar aluno")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Cadastrando aluno...")
            # Aqui você chamaria a sua função vincular_aluno(), por exemplo.
        elif opcao == "2":
            print("Saindo do programa... Até mais!")
            break  # Correção: O break quebra o loop 'while' e encerra a função
        else:
            print("Opção inválida! Tente novamente.")

# Para testar o menu:
menu()