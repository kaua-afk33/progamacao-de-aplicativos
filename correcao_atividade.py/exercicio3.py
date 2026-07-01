import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # 1. Criamos primeiro a tabela 'escolas' (independente)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    ''')

    # 2. Criamos depois a tabela 'series' (que depende de 'escolas')
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

# Para testar a função:
criar_tabelas()
print("Tabelas criadas com sucesso!")