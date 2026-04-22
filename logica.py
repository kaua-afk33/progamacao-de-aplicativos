
def avaliar_desempenho(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota > 5:
        return "Regular"
    else:
        return "Insuficiente"
nota_usuario = float(input("Digite a nota do aluno 0 a 10 "))
menssagem = avaliar_nota(nota)
print(menssagem)