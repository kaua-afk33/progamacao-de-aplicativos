def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        categoria = "Normal"
    elif 25 <= imc <= 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
        
    return f"Relatório: {nome} ({idade} anos) possui IMC de {imc} - Categoria: {categoria}."
n = input("Nome: ")
p = float(input("Peso (kg): "))
a = float(input("Altura (m): "))
i = int(input("Idade: "))

print(gerar_relatorio_saude(n, p, a, i))