import sqlite3
conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()

def cadastrar_aluno():
    nome_completo_aluno = input("Digite o nome completo: ")
    telefone_aluno = input("Digite o telefone: ")
    turma_aluno = input("Digite a Turma: ")
    
    try:
        idade_aluno = int(input("Digite a idade: "))
    except ValueError:
        print("Erro: A idade deve ser um número inteiro. Cadastro cancelado.\n")
        return

    cpf_aluno = input("Digite o cpf: ")
    endereco_aluno = input("Digite o endereço (Rua, Nº): ")
    cidade_aluno = input("Digite a cidade: ")
    estado_aluno = input("Digite o estado (Ex: PR, SC): ")
    
    try:
        professor_id = int(input("Digite o ID do professor: "))
    except ValueError:
        print("Erro: O ID do professor deve ser um número inteiro. Cadastro cancelado.\n")
        return

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT, 
                turma TEXT, 
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL,
                endereco TEXT,
                cidade TEXT,
                estado TEXT,
                professor_id INTEGER,
                FOREIGN KEY (professor_id) REFERENCES professores(id))''')
    
    comando_inserir = f'''
        INSERT INTO alunos(nome, telefone, turma, idade, cpf, endereco, cidade, estado, professor_id)
        VALUES('{nome_completo_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno}, '{cpf_aluno}', '{endereco_aluno}', '{cidade_aluno}', '{estado_aluno}', {professor_id})'''

    cursor.execute(comando_inserir)
    conexao.commit()
    print("Aluno cadastrado com sucesso!\n")

def listar():
    conexao.commit()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(f"{aluno[0]}, nome: {aluno[1]}, telefone: {aluno[2]}, turma: {aluno[3]}, idade: {aluno[4]}, CPF: {aluno[5]}, endereço: {aluno[6]}, cidade: {aluno[7]}, estado: {aluno[8]}, professor: {aluno[9]}")
    print("\n")

def buscar():
    try:
        id_aluno = int(input("Digite o id do aluno: "))
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.\n")
        return

    cursor.execute(f"SELECT * FROM alunos WHERE id = {id_aluno}")

    aluno = cursor.fetchone()
    if aluno:
        print("Aluno encontrado ")
        print(aluno)
    else:
        print("Aluno não encontrado")
    print("\n")

def atualizar():
    try:
        id_aluno = int(input("Digite o id do aluno: "))
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.\n")
        return

    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    nova_turma = input("Digite a nova turma: ")
    
    try:
        nova_idade = int(input("Digite a nova idade: "))
    except ValueError:
        print("Erro: A idade deve ser um número inteiro. Atualização cancelada.\n")
        return

    novo_cpf = input("Digite o novo CPF: ")
    novo_endereco = input("Digite o novo endereço: ")
    nova_cidade = input("Digite a nova cidade: ")
    novo_estado = input("Digite o novo estado (Ex: PR, SC): ")
    
    try:
        novo_professor = int(input("Digite o ID do novo professor: "))
    except ValueError:
        print("Erro: O ID do professor deve ser um número inteiro. Atualização cancelada.\n")
        return

    cursor.execute(f'''
                    UPDATE alunos
                    SET nome = '{novo_nome}', 
                        telefone = '{novo_telefone}', 
                        turma = '{nova_turma}', 
                        idade = {nova_idade}, 
                        cpf = '{novo_cpf}', 
                        endereco = '{novo_endereco}', 
                        cidade = '{nova_cidade}', 
                        estado = '{novo_estado}', 
                        professor_id = {novo_professor} 
                    WHERE id = {id_aluno}''')
    conexao.commit()
    print("Dados atualizados com sucesso!\n")


def remover():
    try:
        id_aluno = int(input("Digite o ID do aluno que deseja remover: "))
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.\n")
        return

    cursor.execute(f"DELETE FROM alunos WHERE id = {id_aluno}")

    conexao.commit()
    if cursor.rowcount > 0 :
        print("Aluno removido com sucesso.\n")
    else:
        print("Nenhum aluno encontrado com esse ID.\n")

opcao_while = 0
while True:
    print("1 - CADASTRAR ALUNO\n2 - LISTAR ALUNOS\n3 - BUSCAR ALUNO\n4 - ATUALIZAR DADOS\n5 - EXCLUIR CADASTRO\n6 - FECHAR PROGRAMA ")
    
    try:
        opcao_while = int(input("Qual ação deseja realizar: "))
    except ValueError:
        print("Opção inválida! Digite apenas números de 1 a 6.\n")
        continue

    if opcao_while == 1:
        cadastrar_aluno()
    elif opcao_while == 2:
        listar()
    elif opcao_while == 3:
        buscar()
    elif opcao_while == 4:
        atualizar()
    elif opcao_while == 5:
        remover()
    elif opcao_while == 6:
        conexao.close()
        break