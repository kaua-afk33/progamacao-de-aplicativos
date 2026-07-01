import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    # Lista de tabelas permitidas para evitar ataques de SQL Injection
    tabelas_permitidas = ["alunos", "professores", "escolas", "series", "turmas"]
    
    if nome_tabela not in tabelas_permitidas:
        print("Erro: Nome de tabela inválido ou não permitido!")
        return

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Correção: O nome da tabela entra via f-string, mas o ID continua seguro via '?'
    query = f"SELECT * FROM {nome_tabela} WHERE id = ?"
    cursor.execute(query, (id_registro,))

    resultado = cursor.fetchone()
    print(resultado)

    conexao.close()

# Exemplo de uso:
# buscar_dados_dinamicos("alunos", 3)