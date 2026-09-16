def busca_sequencial(vetor, alvo):
    comparacoes = 0
    for i in range(len(vetor)):
        comparacoes += 1
        if vetor[i] == alvo:
            return i, comparacoes
    return -1, comparacoes


def busca_binaria(vetor, alvo):
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


vetor_100 = [i * 2 for i in range(1, 101)]



alvos = [
    vetor_100[5],  
    vetor_100[50],  
    vetor_100[95]   
]

print("--- COMPARAÇÃO ENTRE BUSCA SEQUENCIAL E BINÁRIA ---")
print(f"Tamanho do vetor: {len(vetor_100)} elementos\n")

for alvo in alvos:
    
    indice_seq, comp_seq = busca_sequencial(vetor_100, alvo)
    
    indice_bin, comp_bin = busca_binaria(vetor_100, alvo)
    
    print(f"Alvo buscado: {alvo}")
    print(f"  > Sequencial: encontrou no índice {indice_seq} | Comparações: {comp_seq}")
    print(f"  > Binária:    encontrou no índice {indice_bin} | Comparações: {comp_bin}")
    print("-" * 50)
