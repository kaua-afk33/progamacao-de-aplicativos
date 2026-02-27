saldo = float(input("digite o seu saldo"))
idade = int(input("digite a sua idade"))

if idade >= 18 and saldo >= 50.0:
    print("pode entrar no parque")
elif idade < 18 and saldo >= 50.0:
    print("nao pode entrar")
elif idade >= 18 and saldo <= 50.0:
    print("voce nao pode entrar")