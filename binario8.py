def busca_binaria_com_contador(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0 

    while inicio <= fim:
        comparacoes += 1  
        meio = (inicio + fim) // 2

        if vetor[meio] == alvo:
            return meio, comparacoes  
        elif vetor[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes  
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

alvo = 60
indice, total_comparacoes = busca_binaria_com_contador(numeros, alvo)

print(f"Elemento {alvo} encontrado no índice: {indice}")
print(f"Número de comparações necessárias: {total_comparacoes}")