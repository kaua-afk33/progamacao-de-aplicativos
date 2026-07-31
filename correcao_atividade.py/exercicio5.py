import sqlite3
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()
def vincular_aluno_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    nome = input("Nome do aluno: ")

    try:
        id_turma = int(input("Digite o ID numérico da turma: "))
        
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except ValueError:
        print("Erro no banco de dados!")

    finally:
        conexao.close()

vincular_aluno_turma()

# int input foi colocada antes da abertura do bloco try. Se o usuário digitar uma letra, o Python lança um erro ValueError e fecha o programa imediatamente.
