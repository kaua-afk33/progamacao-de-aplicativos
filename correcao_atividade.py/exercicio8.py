import sqlite3 

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # 1. Cria a tabela se ela não existir (com a sintaxe SQL corrigida)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT
        )
    ''') 

    # 2. Insere o professor recebido por parâmetro na função
    cursor.execute(
        "INSERT INTO professores (nome, cpf) VALUES (?, ?)", 
        (nome, cpf)
    )

    # 3. Salva as alterações e fecha a conexão
    conexao.commit()
    conexao.close()
    print(f"Professor {nome} cadastrado com sucesso!")

# Exemplo de como usar a função:
# cadastrar_professor("Carlos Silva", "123.456.789-00")