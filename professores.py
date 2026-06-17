import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL,
        materia TEXT NOT NULL,
        escola TEXT NOT NULL,
        salario TEXT NOT NULL   
    )''')
conexao.commit()

def registrar_professor():
    print("\n--- Cadastrar Professor ---")
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    cpf = input("Digite o seu CPF: ")
    materia = input("Digite a sua matéria: ")
    telefone = input("Digite o seu telefone: ")
    turma = input("Digite a sua turma: ")
    salario = input("Digite o seu salário: ")
    escola = input("Digite a escola que você trabalha: ")

  
    cursor.execute('''
        INSERT INTO professores (nome, telefone, turma, idade, cpf, materia, escola, salario) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, telefone, turma, idade, cpf, materia, escola, salario))
    
    conexao.commit()
    print("Professor cadastrado com sucesso!")

def ver_professores():
    print("\n--- Professores Cadastrados ---")
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    
    if not professores:
        print("Nenhum professor cadastrado.")
        return

    for professor in professores:
        print(f"ID: {professor[0]} | Nome: {professor[1]} | Telefone: {professor[2]} | Turma: {professor[3]} | Idade: {professor[4]} | CPF: {professor[5]} | Matéria: {professor[6]} | Escola: {professor[7]} | Salário: R$ {professor[8]}")

def atualizar_professores():
    ver_professores()
    print("\n--- Atualizar Professor ---")
    idx = input("Qual ID você quer mudar? ")
    
    cursor.execute("SELECT * FROM professores WHERE id = ?", (idx,))
    professor = cursor.fetchone()
    
    if not professor:
        print("Professor não encontrado!")
    else:
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone: ")
        nova_turma = input("Digite a nova turma: ")
        nova_idade = int(input("Digite a nova idade: "))
        novo_cpf = input("Digite o novo CPF: ")
        nova_materia = input("Digite a nova matéria: ")
        nova_escola = input("Digite a nova escola: ")
        novo_salario = input("Digite o novo salário: ")

        cursor.execute('''
            UPDATE professores 
            SET nome = ?, telefone = ?, turma = ?, idade = ?, cpf = ?, materia = ?, escola = ?, salario = ?
            WHERE id = ?
        ''', (novo_nome, novo_telefone, nova_turma, nova_idade, novo_cpf, nova_materia, nova_escola, novo_salario, idx))
        
        conexao.commit()
        print("Professor atualizado com sucesso!")

def deletar_professor():
    ver_professores()
    print("\n--- Excluir Professor ---")
    id_professor = int(input("Digite o ID que você queira excluir: "))
    
    cursor.execute("DELETE FROM professores WHERE id = ?", (id_professor,))
    conexao.commit()
    print("Professor excluído com sucesso!")

while True:
    print("\n--------MENU-------")
    print("1: Criar Professor")
    print("2: Listar Professores")
    print("3: Atualizar Professor")
    print("4: Excluir Professor")
    print("5: Sair")
    
    op = input("Escolha uma opção: ")

    if op == '1':
        registrar_professor()
    elif op == '2':
        ver_professores()
    elif op == '3':
        atualizar_professores()
    elif op == '4':
        deletar_professor()
    elif op == '5':
        print("Saindo do sistema")
        conexao.close()
        break

    else:
        print("Opção inválida.")