 def buscar_nome(alunos, nome):
    i = 0

    while i < len(alunos):
        if alunos[i] == nome:
            return True

        i = i + 1

    return False


alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]

nome = input("Digite o nome do aluno: ")

if buscar_nome(alunos, nome):
    print("Aluno encontrado!")
else:
    print("Aluno não encontrado.")

