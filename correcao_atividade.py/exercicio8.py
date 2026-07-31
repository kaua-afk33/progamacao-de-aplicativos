import sqlite3 
def cadastrar_professor(nome, cpf): 
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 

    cursor.execute(''' 
    	CREATE TABLE IF NOT EXISTS professores ( 
        	id INTEGER PRIMARY KEY AUTOINCREMENT, 
        	nome TEXT, 
            cpf TEXT UNIQUE
        ) 
	''') 

    cadastrar_professor(nome, cpf)

# O campo de CPF foi criado sem a regra que impede valores repetidos no banco.