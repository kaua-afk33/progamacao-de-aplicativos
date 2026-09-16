def busca_binaria(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == alvo:
            return meio 
        elif vetor[meio] < alvo:
            inicio = meio + 1 
        else:
            fim = meio - 1 

    return -1  


numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

alvo_presente = 60
indice_presente = busca_binaria(numeros, alvo_presente)
print(f"Elemento {alvo_presente} encontrado no índice: {indice_presente}")

alvo_ausente = 25
indice_ausente = busca_binaria(numeros, alvo_ausente)
print(f"Elemento {alvo_ausente} encontrado no índice: {indice_ausente}")