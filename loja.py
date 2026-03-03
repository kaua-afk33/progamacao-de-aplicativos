valor_da_compra = float(pinput("digite o valor da compra"))
prime = input("voce e cliente prime (S/N)")
frete = 50.00

if valor_da_compra > 500.00 or (prime == "S" and valor_da_compra > 100.00):
    print("voce ganhou frete gratis")
frete = 0.00
print("valor da compra" , valor_da_compra)

valor_total = valor_da_compra + frete
print("valor_compra" , valor_total)

