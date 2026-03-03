nome = input("seu nome")
senha = int(input("sua senha"))

if nome == ("admin" or nome == "root") and senha == 1234:
    print("acesso liberado")

else:
    print("acesso negado")