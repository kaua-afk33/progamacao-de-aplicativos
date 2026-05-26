import json
import os

matricula = 'aluno'


def cadastrar_aluno():
    print("/n---nova matricula---")

    if os.path.exists(aluno_dados):
        with open (aluno_dados, 'w' , encoding= 'utf -8') as f:
            aluno = json.load(f)
    else:
        aluno = []
    aluno = {
        "nome": input("Nome: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: "), 
        "id": int(input("id")).
    }


    aluno.append(novo_aluno)

    with open(dados, 'w' encoding= 'utf-8') as f:
        json.dump(aluno, f, indent=4)
            for aluno in alunos:
                print("aluno cadastrado")
                    return