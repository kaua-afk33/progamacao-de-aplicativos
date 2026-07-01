import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


urgente:
    cursor.execute("UPDATE  alunos SET nome = ?", (novo_nome,))


conexao.commit()
conexao.close()