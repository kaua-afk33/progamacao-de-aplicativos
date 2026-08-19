def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"

assert situacao_aluno(8.5) == "Aprovado", "Falhou: Média 8.5 deveria ser Aprovado"

assert situacao_aluno(6) == "Aprovado", "Falhou: Média 6 deveria ser Aprovado"

assert situacao_aluno(5.9) == "Recuperação", "Falhou: Média 5.9 deveria ser Recuperação"

assert situacao_aluno(4) == "Recuperação", "Falhou: Média 4 deveria ser Recuperação"

assert situacao_aluno(3.5) == "Reprovado", "Falhou: Média 3.5 deveria ser Reprovado"

print("Todos os testes para 'situacao_aluno' passaram com sucesso!")