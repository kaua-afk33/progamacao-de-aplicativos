import sqlite3 

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

cursor.execute('''
    CREAT TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENTE,
        nome TEXT,
        cpf TEXT
    (
''')