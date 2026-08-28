from cooperativa import cadastrar_cooperativa, listar_dados, deletar_cooperativa, atualizar_cooperativa
from silos import cadastrar_silos, listar_silos, deletar_silos, atualizar_silos




   
while True:
    print("\n" + "=" * 40)
    print(" MENU PRINCIPAL ")
    print("=" * 40)
    print("1| Cadastrar Cooperativa")
    print("2| Cadastrar Silos")
    print("3| Listar Geral (Cooperativas e Silos)")
    print("4| Listar Apenas Silos")
    print("5| Atualizar Cooperativa")
    print("6| Atualizar Silo")
    print("7| Deletar Cooperativa")
    print("8| Deletar Silo")
    print("9| Sair")

    opcao = input("\nEscolha a opção: ")

    if opcao == "1":
        cadastrar_cooperativa()
    elif opcao == "2":
        cadastrar_silos()
    elif opcao == "3":
        listar_dados()
    elif opcao == "4":
        listar_silos()
    elif opcao == "5":
        atualizar_cooperativa()
    elif opcao == "6":
        atualizar_silos()
    elif opcao == "7":
        deletar_cooperativa()
    elif opcao == "8":
        deletar_silos()
    elif opcao == "9":
        print("\nSaindo do menu...")
        break
    else:
        print("\nOpção inválida, tente novamente!")

menu()
conexao.close()