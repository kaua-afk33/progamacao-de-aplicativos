import sqlite3

def inicializar_banco():
    """Conecta ao banco de dados, ativa as chaves estrangeiras e cria as tabelas se não existirem."""
    try:
        conexao = sqlite3.connect("hotelaria.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hoteis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS quarto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                preco_diaria REAL NOT NULL,
                id_hotel INTEGER NOT NULL,
                FOREIGN KEY (id_hotel) REFERENCES hoteis(id)
            );
        """)
        
        conexao.commit()
        print(" Banco de dados inicializado com sucesso!")
        return conexao
    except sqlite3.Error as e:
        print(f" Erro ao inicializar o banco de dados: {e}")
        return None

def cadastrar_hotel(conexao):
    try:
        cursor = conexao.cursor()
        print("\n--- Cadastro de Novo Hotel ---")
        nome = input("Digite o nome do hotel: ")
        cidade = input("Digite a cidade do hotel: ")
        
        cursor.execute("INSERT INTO hoteis (nome, cidade) VALUES (?, ?)", (nome, cidade))
        conexao.commit()
        print(f" Hotel '{nome}' cadastrado com sucesso! ID gerado: {cursor.lastrowid}")
    except sqlite3.Error as e:
        print(f" Erro no banco de dados ao cadastrar hotel: {e}")

def cadastrar_quarto(conexao):
    """Cadastra um quarto recebendo dados via input e aplicando tratamento duplo de exceções."""
    try:
        print("\n--- Cadastro de Novo Quarto ---")
        numero = int(input("Digite o número do quarto: "))
        preco_diaria = float(input("Digite o preço da diária (ex: 150.00): "))
        id_hotel = int(input("Digite o ID do hotel ao qual este quarto pertence: "))
        
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO quarto (numero, preco_diaria, id_hotel) VALUES (?, ?, ?);",
            (numero, preco_diaria, id_hotel)
        )
        
        conexao.commit()
        print(" Quarto cadastrado com sucesso!")
        
    except ValueError:
        print(" Erro de digitação: Você digitou letras ou caracteres inválidos em um campo numérico. Tente novamente.")
        
    except sqlite3.Error as e:

        print(f" Erro no Banco de Dados: {e}")
        print(" Dica: Verifique se o ID do hotel informado realmente existe na tabela de hotéis.")

def listar_hoteis(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, cidade FROM hoteis;")
        hoteis = cursor.fetchall()
        
        print("\n--- Lista de Hotéis Cadastrados ---")
        if not hoteis:
            print("Nenhum hotel cadastrado no momento.")
            return
        
        for h in hoteis:
            print(f"ID: {[0]} | Nome: {[1]} | Cidade: {[2]}")
            
    except sqlite3.Error as e:
        print(f" Erro ao listar hotéis: {e}")

def menu():
    conexao = inicializar_banco()
    if not conexao:
        return

    try:
        while True:
            print("\n-------------MENU DO HOTEL-------------")
            print("1. Cadastrar Hotel")
            print("2. Listar Hotéis")
            print("3. Cadastrar Quarto")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                cadastrar_hotel(conexao)
            elif opcao == "2":
                listar_hoteis(conexao)
            elif opcao == "3":
                cadastrar_quarto(conexao)
            elif opcao == "4":
                print("Encerrando o sistema... Até logo!")
                break
            else:
                print(" Opção inválida! Escolha um número entre 1 e 4.")
    finally:
        conexao.close()

if __name__ == "__main__":
    menu()