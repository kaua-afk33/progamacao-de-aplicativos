def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"

assert situacao_aluno(6) == "Aprovado"

assert situacao_aluno(5.9) == "Reprovado"

assert situacao_aluno(0) == "Reprovado"

assert situacao_aluno(10) == "Aprovado"

assert situacao_aluno(6.10) == "Aprovado"

print("todos foi aprovados")