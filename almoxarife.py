usuario = ["pedro" , "felipe" , "carlos" , "vitor"]
usarios = []

print("1 adicone o usario")
print("2 entrar")
print("3 sair")

opcao = input("escolha uma opcao")
while opcao != "3":
    if opcao == "1":
        usuario = input("digite o nome do usuario")
        senha = input("digite a senha")

        if usuario in usuario:
            print("usuarios ja existe")
        else:
            usuario[usuario] = senha
            print("usuario foi cadastrado")

        opcao = input("escolha uma opcao")

    elif opcao == "2":
        usuario = input("usuario")
        senha = input("senha")

        if usuario in usuario and usuarios[usuarios] == senha:
            print(f"bem vindo , {usuarios}")
        else:
            print("usuario incorreto")

        opcao = input("escolha uma opcao")
            
    elif opcao == "3":
        print("saindo do sistema")
    else:
        print("opcao errada")

        print("saindo do sistema")
