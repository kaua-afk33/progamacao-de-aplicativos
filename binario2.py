2 lista = [5, 8, 5, 3, 5, 9, 2, 5, 10, 6]

valor = int(input("Digite o valor que deseja buscar: "))

i = 0
contador = 0

while i < 10:
    if lista[i] == valor:
        contador = contador + 1

    i = i + 1

print("O valor aparece", contador, "vezes na lista.")




