import sqlite3

try:
    conexao = sqlite3.connect('escola_demonstraçao.db')
    cursor = conexao.cursor()
except ValueError:
    print("erro de conexao")


cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS professores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT NOT  NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL,
        salario REAL NOT NULL,
        nome_da_escola TEXT NOT NULL
    )
''')

def registrar_professor(): 
    nome_professor =input("digite seu nome: ")
    telefone_professor =input("digite seu telefone: ")
    idade_professor =int(input("digite sua idade: "))
    materia_professor =input("digite sua turma: ")
    cpf_professor =input("digite seu cpf: ")
    salario_professor =float(input("digite seu salario: "))
    nome_da_escola = input("digite o nome da escola: ")
    cursor.execute('''
        INSERT INTO professor (nome, telefone, materia, idade, cpf, salario, nome_da_escola) VALUES (?, ?, ?, ?, ?)
    ''', (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_da_escola))
    conexao.commit()
    print("professor cadastrado com sucesso")


def ver_professores():
    print("\n--- PROFESSORES CADASTRADOS ---")
    cursor.execute("SELECT * FROM professores")
    for professor in cursor.fetchall():
        print(professor)


def atualizar_professores():
    ver_professores()

    print("\n--- ATUALIZAR PROFESSORES ---")

    idx = int(input("qual id deseja atualizar?"))

    cursor.execute("SELECT * FROM professores WHERE id = ?", (idx))

    professor = cursor.fetchone()

    if not professor:
        print("professor não encontrado")
    else:
        nome_professor =input("digite seu nome: ")
    telefone_professor =input("digite seu telefone: ")
    idade_professor =int(input("digite sua idade: "))
    materia_professor =input("digite sua turma: ")
    cpf_professor =input("digite seu cpf: ")
    salario_professor =float(input("digite seu salario: "))
    nome_da_escola = input("digite o nome da escola: ")

    cursor.execute("UPDATE professores SET nome_completo = ?, telefone = ?, materia = ?, idade = ?, cpf = ?, salario = ?, nome_da_escola = ?",
    (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_da_escola))
    conexao.commit()
    print("--- PROFESSOR ATUALIZADO COM SUCESSO ---")