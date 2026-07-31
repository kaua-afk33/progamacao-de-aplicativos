import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id_escola INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            )
        ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_serie TEXT,
        id_escola INTEGER,
        FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    ''')

        
    conexao.commit()
    conexao.close()

    criar_tabelas()

# Tentativa de criar uma tabela filha que faz referência a uma tabela pai que ainda não existe no código.