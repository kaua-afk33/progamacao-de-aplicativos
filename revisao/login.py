senha_correta = "python123"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Digite a senha: ")
    
    if tentativa != senha_correta:
        print("Senha incorreta! Tente novamente.")

print("Bem-vindo!")
