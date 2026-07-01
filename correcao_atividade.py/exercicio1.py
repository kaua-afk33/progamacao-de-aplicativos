import sqlite3

# 1. Estabelece a conexão com o banco de dados
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

# 2. Cria a tabela (Corrigido: 'CREATE' com 'E' no final)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')

# 3. Definição da função para capturar e cadastrar o nome da escola
def cadastrar_escola():
    nome_escola = input("Digite o nome da escola: ")
    
    # Insere o nome no banco de dados
    # Como o ID é AUTOINCREMENT, não precisamos passar ele manualmente!
    cursor.execute(
        "INSERT INTO escolas (nome) VALUES (?)", 
        (nome_escola,)
    )
    
    # Salva as alterações na sessão atual
    conexao.commit()
    print(f"Escola '{nome_escola}' cadastrada com sucesso!")

# --- Exemplo de Uso ---
# Para testar, você pode chamar a função aqui:
# cadastrar_escola()

# 4. Fecha a conexão com o banco de dados ao final do programa
conexao.close()