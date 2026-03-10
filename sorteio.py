id = input("digite o id")
valor_compra = float(input("digite o valor da compra"))

if id % 2 == 0 and valor_compra >= "500.00":
    print("parabens, {id} voce ganhou cupom para sua compra de R$ {valor}")

else:
    print("brigado pela compra {id} continue acompanhando as nossas promocoes")