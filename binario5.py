 def buscar_posicoes(vetor, numero):
    i = 0
    primeira = -1
    ultima = -1

    while i < len(vetor):
        if vetor[i] == numero:
            if primeira == -1:
                primeira = i

            ultima = i

        i = i + 1

    return primeira, ultima
 

vetor = [5, 8, 3, 5, 9, 5, 2, 7, 5, 6]

numero = int(input("Digite o número que deseja buscar: "))

primeira, ultima = buscar_posicoes(vetor, numero)

if primeira != -1:
    print("Primeira posição:", primeira)
    print("Última posição:", ultima)
else:
    print("Número não encontrado.")

