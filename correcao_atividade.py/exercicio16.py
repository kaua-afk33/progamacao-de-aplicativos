def menu(): 
    while True: 
        print("1. Cadastrar Aluno") 
        print("2. Sair") 
        opcao = input("Escolha: ") 
         
        if opcao == "1": 
            print("Cadastrando...") 
        elif opcao == "2": 
            print("Saindo do programa.") 
            break
        	
            pass 
menu()

# O comando pass é apenas um preenchedor de código e não encerra um laço de repetição while True.