import sqlite3 

def criar_tabela_turma(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS turmas ( 
        	id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_turma TEXT, 
            id_serie INTEGER NOT NULL,  
            FOREIGN KEY (id_serie) REFERENCES series(id) 
        ) 
    ''') 
    conexao.commit() 
    conexao.close() 

criar_tabela_turma()

# A coluna que representa a chave estrangeira foi criada na tabela sem declarar o seu tipo de dado (como INTEGER).