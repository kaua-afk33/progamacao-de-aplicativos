1 vetor = [5, 8, 12, 3, 9, 15, 7, 2, 10, 6]

numero = int(input("Digite o número que deseja buscar: "))

i = 0

while i < 10:
    if vetor[i] == numero:
        print("Número encontrado no índice:", i)
        break

    i = i + 1
