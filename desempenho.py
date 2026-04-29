def analisar_vendas(nome, lista_vendas, meta_mensal):
    media = sum(lista_vendas) / len(lista_vendas)
    bateu_meta = media >= meta_mensal
    status = "bateu" if bateu_meta else "não bateu"
    
    return f"O vendedor {nome} teve média de {media:.2f} e {status} a meta."

nome_vendedor = "Carlos"
vendas = [1200, 1500, 1100, 1900]
meta = 1400

print(analisar_vendas(nome_vendedor, vendas, meta))