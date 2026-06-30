import sqlite3

def vincular_aluno():
    nome = input("nome do aluno")

try:
    id_turma = int(input("digite o ID numerico da turma"))

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("erro no bancos de dados")
        finally:
            conexao.close()