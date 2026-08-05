import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect("defesa_central.db")
        cursor = conexao.cursor()

    conexao.execute ('''
                CREAT TABLE IF NOT EXIST defesa_central (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome NOT NULL,
                    cidade NOT NULL
                )
            ''')