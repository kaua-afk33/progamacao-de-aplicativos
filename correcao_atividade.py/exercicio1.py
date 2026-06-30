import sqlite3

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()


cursor.execute('''
    CREAT TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')

def nome():
    n = input("digite o seu nome")

conexao.close()