nome = input("Digite o nome do cliente: ")
valor_original = float(input("Digite o valor total da compra (R$): "))
distancia = int(input("Digite a distância da entrega (km): "))
tem_cupom = input("Possui cupom especial? (S/N): ").strip().upper()

desconto_percentual = 0.0
ganhou_brinde = False

if valor_original >= 1.000 and tem_cupom == "S":
    desconto_percentual = 0.20
    ganhou_brinde = True
elif 500 < valor_original < 1.000 and tem_cupom == "S":
    desconto_percentual = 0.10

valor_desconto = valor_original * desconto_percentual
valor_com_desconto = valor_original - valor_desconto

if distancia <= 50 and valor_com_desconto > 200:
    valor_frete = 0.00
else:
    valor_frete = 40.00

total_final = valor_com_desconto + valor_frete

print("\n" + "="*30)
print("RESUMO DA COMPRA")
print("="*30)
print("Cliente: nome")
print("Valor Original:" , valor_original)
print("Desconto Aplicado:" , valor_desconto)
print("Custo de Frete:" , valor_frete)
print("TOTAL FINAL:" , total_final)
print("="*30)

if ganhou_brinde:
    print("Parabéns Você ganhou um Mouse pad Gamer de brinde")