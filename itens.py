def esta_na_lista(lista, nome_para_buscar):

    for item in lista:
        if item == nome_para_buscar:
            return "Encontrado!"
    return "Não disponível"

frutas = ["maçã", "banana", "laranja", "uva", "melancia"]

busca1 = "uva"     
resultado1 = esta_na_lista(frutas, busca1)
print(f"Busca por {busca1}: {resultado1}")

busca2 = "pera"
resultado2 = esta_na_lista(frutas, busca2)
print(f"Busca por {busca1}'{busca2} {resultado1}")

busca3 = "maçã"
print(f"Busca por{busca3}: {esta_na_lista(frutas, busca3)}")
