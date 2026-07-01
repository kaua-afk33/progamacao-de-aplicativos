import sqlite3

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escola (nome) VALUES (?)",  (nome,))
    conexao.commit()
    