import sqlite3


conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
    CREAT TABLE IN NOT EXIST professores)
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXY NOT  NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
        materia TEXT UNIQUE NOT NULL
        escola TEXT UNIQUE NOT NULL
        salario TEXT UNIQUE NOT NULL      
    )
''')

def registrar_professor():

    nome = input("digite o seu nome")
    idade = int(input("digite a sua idade"))
    cpf = input("digite o seu cpf")
    materia = input("digite a sua materia")
    telefone = input("digite o seu telefone")
    salario = float(input("digite o seu salario"))
    escola = input("digite a escola que voce trabalha")

    cursor('''
        INSERT INTO professores (nome, telefone, turma, idade, cpf) VALUES (?, ?, ?, ?, ?)
    ''' , (nome_professor, telefone_professor, turma_professor, cpf_professor, idade_professor, salario_professor, materia_professor, escola_professor))
    conexao.commit()
    print("professor cadastrado com sucesso")

def ver_professor():
    print("\n professores cadastrados")
    crusor.execute("SELECT * FROM professores")
    for professor in cursor.fetchall():
        print(professor)

def atualizar_professsores():
    ver_professor()
    print("\n ver professor")
    idx = input("qual id voce quer mudar")
    cursor.execute(
        "SELECT * FROM professores WHERE id = ?", (idx,)
    )
    professor = cursor.fetchone()
    if professor:
        novo_nome = input("digite o novo nome")
        novo_cpf = input("digite o novo cpf")
        nova_idade = int(input("digite a nova idade"))
        novo_telefone = input("digite o seu novo telefone")
        novo_salario = float(input("digite o novo salario"))
        nova_escola = input("digite a sua nova escola")
        nova_materia = input("digite a sua nova materia")

conexao.comimt()
conexao.clone()