nome_usario = input("nome do usario")
codigo_secreto = int(input("digite o codigo"))

if nome_usario == "admim" and codigo_secreto == 999:
    print("pode entrar")
else:
    print("falha no codigo")