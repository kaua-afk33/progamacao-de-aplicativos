import sqlite3 


def inserir_escola(nome): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,)) 
    conexao.commit() 

nome = input("Digite o nome da escola: ")

# Criar a conexão com o banco como uma variável global no início do arquivo dificulta a manutenção e gera conflitos quando múltiplos módulos tentam usar o banco ao mesmo tempo