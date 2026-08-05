import sqlite3

conexao = sqlite3.connect('cinemas.db')
cursor = conexao.cursor()

def criar_tabelas_cinema():
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cinema TEXT NOT NULL,
            shopping TEXT NOT NULL
    )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_sala INTEGER NOT NULL,
            capacidade INTEGER NOT NULL,
            id_cinemas INTEGER NOT NULL,
            FOREIGN KEY (id_cinemas) REFERENCES cinemas(id)
        )''')
    conexao.commit()

def cadastrar_cinema():
    try:
        print("\n ---CINEMA--- ")
        nome_cinema = input("QUAL O NOME DO SEU CINEMA?: ")
        shopping = input("EM QUAL SHOPPING SE ESTABELECE LOCALIZADO?: ")

        cursor.execute("INSERT INTO cinemas (nome_cinema, shopping) VALUES (?, ?)", 
                        (nome_cinema, shopping))
        conexao.commit()
        print("\n ---Cinema cadastrado com sucesso!!!--- ")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar cinemas: {e}")

def cadastrar_salas():
    try:
        print("\n ---SALAS--- ")
        numero_sala = int(input("QUAL O NUMERO DA SUA SALA?: "))
        capacidade = int(input("QUAL A CAPACIDADE DA SALA?: "))
        id_cinemas = int(input("QUAL O ID DO CINEMA?: "))

        cursor.execute("INSERT INTO salas (numero_sala, capacidade, id_cinemas) VALUES (?, ?, ?)",
                        (numero_sala, capacidade, id_cinemas))
        conexao.commit()
        print("\n ---Sala cadastrada com sucesso!!!--- ")
    except sqlite3.IntegrityError:
        print("Erro: ID do CINEMA inexistente!")
    except ValueError:
        print("Erro: CAPACIDADE, ID e NUMERO DA SALA devem ser números inteiros!")

def listar_dados():
    print("\n" + "="*40)
    print(" 📋 LISTA DE CINEMAS E SALAS CADASTRADAS ")
    print("="*40)

    cursor.execute('''
        SELECT c.id, c.nome_cinema, c.shopping, s.numero_sala, s.capacidade
        FROM cinemas c
        LEFT JOIN salas s ON c.id = s.id_cinemas
    ''')
    
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Nenhum registro encontrado.")
        return

    cinema_atual = None
    for linha in resultados:
        id_cine, nome_cine, shopping, num_sala, capacidade = linha
        
        if cinema_atual != id_cine:
            cinema_atual = id_cine
            print(f"\n🎬 Cinema ID: {id_cine} | Nome: {nome_cine} | Shopping: {shopping}")
            print(f"   Salas:")
        
        if num_sala is not None:
            print(f"    - Sala nº {num_sala} (Capacidade: {capacidade} pessoas)")
        else:
            print(f"    - Nenhuma sala cadastrada para este cinema.")
    
    print("\n" + "="*40)

criar_tabelas_cinema()
cadastrar_cinema()
cadastrar_salas()
listar_dados() 

conexao.close()