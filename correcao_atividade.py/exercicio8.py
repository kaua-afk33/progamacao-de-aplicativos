import sqlite3

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS professores;")

cursor.execute(''' 
    CREATE TABLE professores ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT, 
        cpf TEXT UNIQUE 
    ) 
''')

conexao.commit()
conexao.close()

print("Tabela 'professores' recriada com sucesso com a coluna CPF!")