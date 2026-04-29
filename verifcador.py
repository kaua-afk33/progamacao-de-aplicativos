def par(numero):
    return numero % 2 == 0

numero = int(input("Digite um número: "))

if par(numero):
    print("Este número é par")
else:
    print("Este número é ímpar")
