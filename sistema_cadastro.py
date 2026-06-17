
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
def registrar_aluno():

    nome_aluno =input("digite seu nome: ")
    telefone_aluno =input("digite seu telefone: ")
    idade_aluno =int(input("digite sua idade: "))
    turma_aluno =input("digite sua turma: ")
    cpf_aluno =input("digite seu cpf: ")

    cursor.execute('''
        INSERT INTO alunos (nome, telefone, turma, idade, cpf) VALUES (?, ?, ?, ?, ?)
    ''', (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno))
    conexao.commit()
    print("aluno cadastrado com sucesso")

def ver_alunos():
    print("\n--- ALUNOS CADASTRADOS ---")
    cursor.execute("SELECT * FROM alunos")
    for aluno in cursor.fetchall():
        print(aluno)

def atualizar_alunos():
    ver_alunos()
    print("\n ver alunos")
    idx = input("qual id voce quer mudar")
    cursor.execute(
        "SELECT * FROM alunos WHERE id = ?", (idx,)
    )
    aluno = cursor.fetchone()
    if aluno:
        novo_nome = input("qual e o novo nome")
        novo_telefone = input("digite o novo numero de telefone")
        nova_idade = int(input("digite a sua nova idade"))
        nova_turma = input("digite a nova turma")
        novo_cpf = input("digite o novo cpf")

def deletar_professor():
    

