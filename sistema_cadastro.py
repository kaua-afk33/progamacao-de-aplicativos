import sqlite3

conexao = sqlite3.connect('escola_demonstraçao.db')
cursor = conexao.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXY NOT  NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
''')

nome_aluno =input("digite seu nome: ")
telefone_aluno =input("digite seu telefone: ")
idade_aluno =int(input("digite sua idade: "))
turma_aluno =input("digite sua turma: ")
cpf_aluno =input("digite seu cpf: ")


cursor.execute('''
    INSERT INTO alunos (nome, telefone, turma, idade, cpf) VALUES (?, ?, ?, ?, ?)
''', (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno))
conexao.commit()


print("\n--- ALUNOS CADASTRADOS ---")
cursor.execute("SELECT * FROM alunos")

for aluno in cursor.fetchall():
    print(aluno)

conexao.close()