altura = float(input("digite a sua altura"))
peso = int(input("digite o seu peso"))

imc = (peso / altura)
print("voce esta no peso")
if peso > 25:
    print("voce esta acima do peso")