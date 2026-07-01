import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    # Toda a lógica agora está corretamente alinhada dentro da função (4 espaços)
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    
    # Ativa o suporte a chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON;") 
    
    # Insere os dados na tabela
    cursor.execute(
        "INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", 
        (nome, id_serie, id_prof)
    )
    
    # Salva as alterações e fecha a conexão
    conexao.commit()    
    conexao.close()

# Exemplo de como chamar a função:
# cadastrar_turma("8º Ano A", 2, 5)