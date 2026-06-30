exercicio 3

import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,    
            nome_serie text, 
            ID_ESCOLA integer,
            FOREIGN KEY (id_escola REFERENCES escolas(id)
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    ''')
    conexao.commit()
    conexao.close()