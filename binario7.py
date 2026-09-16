def busca_binaria_palavra(lista_palavras, alvo):
    inicio = 0
    fim = len(lista_palavras) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        palavra_meio = lista_palavras[meio]

        if palavra_meio == alvo:
            return meio 
        elif palavra_meio < alvo:
            inicio = meio + 1  
        else:
            fim = meio - 1  

    return -1  


vocabulario = ["abacate", "banana", "cereja", "damasco", "figo", "goiaba", "kiwi", "manga"]

alvo_presente = "figo"
indice_presente = busca_binaria_palavra(vocabulario, alvo_presente)
print(f"A palavra '{alvo_presente}' está no índice: {indice_presente}")