def encontrar_posicao_insercao(vetor, alvo):
    inicio = 0
    fim = len(vetor)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if vetor[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio

    return inicio


numeros = [10, 20, 30, 50, 60]
novo_numero = 35

posicao = encontrar_posicao_insercao(numeros, novo_numero)
print(f"O número {novo_numero} deve ser inserido no índice: {posicao}")

numeros.insert(posicao, novo_numero)
print(f"Vetor atualizado: {numeros}")