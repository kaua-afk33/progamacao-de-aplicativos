import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Correção 1: Alinhado todo o bloco para dentro da função (indentação)
    # Correção 2: Corrigido para 'CREATE TABLE IF NOT EXISTS'
    # Correção 3: Adicionado o tipo 'INTEGER' para a coluna id_serie
    # Correção 4: Corrigido para 'FOREIGN KEY'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turma (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT,
            id_serie INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id)
        )
    ''')

    conexao.commit()
    conexao.close()
    print("Tabela 'turma' criada com sucesso!")

# Para testar a função:
# criar_tabela_turma()