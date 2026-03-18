cores = ["Vermelho", "Verde", "Azul", "Amarelo", "Preto"]
entrada = input("Digite um número de 1 a 5 para escolher uma cor: ")

try:
    numero = int(entrada)
    if 1 <= numero <= 5:
        indice = numero - 1
        cor_escolhida = cores[indice]
        print(f"A cor escolhida foi: {cor_escolhida}")
    else:
        print("Número fora do intervalo (1-5).")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
