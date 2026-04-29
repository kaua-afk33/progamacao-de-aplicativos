def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
   
    valor_com_imposto = valor_base + (valor_base * (imposto_percentual / 100))
    
    preco_final = valor_com_imposto - cupom_desconto
    
    if preco_final < 0:
        preco_final = 0
        
    return preco_final

v_base = float(input("Digite o valor base do produto: "))
imp = float(input("Digite o percentual de imposto: "))
cupom = float(input("Digite o valor do cupom de desconto: "))

resultado = calcular_preco_final(v_base, imp, cupom)
print(f"Preço Final: R$ {resultado}")