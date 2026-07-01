import sqlite3

def verificar_registro():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

print("primeiro print:", cursor.fetchall())
print("segundo print:", cursor.fetchall())

conexao.close()