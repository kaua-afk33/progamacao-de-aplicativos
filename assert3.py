def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

assert calcular_desconto(100.0, 0) == 100.0, "Falhou: Sem desconto o preço deve ser o original"

assert calcular_desconto(200.0, 10) == 180.0, "Falhou: 10% de desconto em 200 deveria ser 180"

assert calcular_desconto(50.0, 50) == 25.0, "Falhou: 50% de desconto em 50 deveria ser 25"

assert calcular_desconto(80.0, 100) == 0.0, "Falhou: 100% de desconto deveria zerar o preço"

assert abs(calcular_desconto(49.99, 20) - 39.992) < 1e-5, "Falhou: Cálculo com preço decimal incorreto"

print("Todos os testes para 'calcular_desconto' passaram com sucesso!")