nivel_atual = int(input("digite o seu nivel atual"))
esferas = int(input("digite a quantidade de esfera que voce possui"))

if nivel_atual >= 50 and esferas >= 25:
    print("voce obteve super pulo")
elif nivel_atual < 50 and esferas >= 25:
    print("voce nao tem level sufiente")
elif nivel_atual >= 50 and esferas < 25:
    print("voce nao tem esferas sufiente")