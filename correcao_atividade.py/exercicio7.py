import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
                                                      
conexao = sqlite3.connect('sistema_escola.db')# 1. Abre a conexão e cria o cursor dentro da função
    cursor = conexao.cursor()
    

    cursor.execute("PRAGMA foreign_keys = ON;") # 2. Ativa o suporte a chaves estrangeiras (correção de 'foreing' para 'foreign')
    
   
    cursor.execute(
        "INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", # 3. Insere os dados na tabela
        (nome, id_serie, id_prof)
    )
    
    conexao.commit()    # 4. Salva as alterações e fecha a conexão
    conexao.close()