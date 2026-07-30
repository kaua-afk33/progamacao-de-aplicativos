import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT NOT NULL,
                id_escola INTERGER,
                FOREIGN KEY (id_escola) REFERENCES escolas (id)
            )
        ''')

    conexao.commit()
    conexao.close()
    print("banco de dados iniciado com sucesso")

inicializar_banco()