def gerar_etiqueta(rua, numero, bairro, cidade, cep, urgencia=False):
    etiqueta = ()
        f"RUA: {rua}, Nº: {numero}\n"
        f"BAIRRO: {bairro} - CIDADE: {cidade}\n"
        f"CEP: {cep}"
    
    
    if urgencia:
        etiqueta = "--- [URGENTE] ---\n" + etiqueta
        
    return etiqueta

print(gerar_etiqueta("Av. Paulista", "1000", "Bela Vista", "São Paulo", "01310-100", urgencia=True))