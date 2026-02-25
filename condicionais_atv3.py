compra = float(input("digite o valor da sua compra"))
cupom = input("digite o valor do cupom: ")

desconto = compra * 0.10
valor_desconto = compra - desconto


if cupom == "DEV10":
    print("cupao valido" , valor_desconto)
else:
    print("cupom invalido" , compra)