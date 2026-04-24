def validar_senha(senha):
    while len(senha) < 6:
        print("senha invalida")
        senha = input("digite a senha novamente: ")
    if len(senha) >= 6:
        print("senha cadastrada")

senha_usuario = input("digite a sua senha: ")
validar_senha(senha_usuario)


