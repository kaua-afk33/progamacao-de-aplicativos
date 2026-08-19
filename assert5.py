def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20

assert calcular_frete(50.0) == 20, "Falhou: Compra de 50 deveria custar 20 de frete"

assert calcular_frete(100.0) == 10, "Falhou: Compra de 100 deveria custar 10 de frete"

assert calcular_frete(150.0) == 10, "Falhou: Compra de 150 deveria custar 10 de frete"
assert calcular_frete(199.99) == 10, "Falhou: Compra de 199.99 deveria custar 10 de frete"

assert calcular_frete(200.0) == 0, "Falhou: Compra de 200 deveria ter frete grátis"

assert calcular_frete(500.0) == 0, "Falhou: Compra de 500 deveria ter frete grátis"

print("Todos os testes para 'calcular_frete' passaram com sucesso!")