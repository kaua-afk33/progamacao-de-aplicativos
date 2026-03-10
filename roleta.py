senha = input("digite a sua senha")
tentativa = int(input("digite a sua tentativa atual"))
tokens = input("possui tokens (s/n)")

if senha == "admin123" and tentativa == "3%" or tokens == "s":
    print(f"tentativa nº {tentativa}acesso permetido")

else:
    print(f"tentativa nº {tentativa} acesso negado")