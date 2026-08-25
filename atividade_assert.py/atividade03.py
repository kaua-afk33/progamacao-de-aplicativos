def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100) 

assert calcular_desconto(100, 10) == 90.0   
assert calcular_desconto(200, 50) == 100.0  
assert calcular_desconto(50, 20) == 40.0    

print("Todos os testes passaram com sucesso após a correção!")