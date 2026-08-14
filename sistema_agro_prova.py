import sqlite3

conexao = sqlite3.connect("cooperativa_agricola.db")
cursor = conexao.cursor()


def criar_tabelas_cooperativas():
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cooperativas_mae (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cooperativa TEXT NOT NULL,
            registro_ocb TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS silos_armazenamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            localidade TEXT NOT NULL,
            capacidade INTEGER NOT NULL,
            id_cooperativa INTEGER NOT NULL,
            FOREIGN KEY (id_cooperativa) REFERENCES cooperativas_mae(id)
        )
    """)

    conexao.commit()


def cadastrar_cooperativa():
    try:
        print("\n" + "=" * 40)
        print(" CADASTRO DE COOPERATIVA MÃE ")
        print("=" * 40)
        nome_cooperativa = input("Qual o nome da cooperativa?: ")
        registro_ocb = input("Digite o registro OCB: ")

        cursor.execute(
            "INSERT INTO cooperativas_mae (nome_cooperativa, registro_ocb) VALUES (?, ?)",
            (nome_cooperativa, registro_ocb),
        )
        conexao.commit()
        print("\n Cooperativa cadastrada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar cooperativa: {e}")


def cadastrar_silos():
    try:
        print("\n" + "=" * 40)
        print(" CADASTRO DE SILOS DE ARMAZENAMENTO ")
        print("=" * 40)
        localidade = input("Qual é a localidade do silo?: ")
        capacidade = int(input("Digite a capacidade do silo [toneladas]: "))
        id_cooperativa = int(input("Qual é o ID da cooperativa mãe vinculada?: "))

        cursor.execute(
            "INSERT INTO silos_armazenamento (localidade, capacidade, id_cooperativa) VALUES (?, ?, ?)",
            (localidade, capacidade, id_cooperativa),
        )
        conexao.commit()
        print("\n Silo cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: O ID da cooperativa mãe informado não existe no sistema.")
    except ValueError:
        print("Erro: A capacidade e o ID devem ser números inteiros.")


def listar_dados():
    print("\n" + "=" * 40)
    print(" RELATÓRIO: COOPERATIVAS E SILOS ")
    print("=" * 40)

    cursor.execute("SELECT id, nome_cooperativa, registro_ocb FROM cooperativas_mae")
    coops = cursor.fetchall()

    if not coops:
        print("Nenhuma cooperativa cadastrada.")
        return

    print("\n--- COOPERATIVAS ---")
    for cooperativa in coops:
        print(f"ID: {cooperativa[0]} | Nome: {cooperativa[1]} | OCB: {cooperativa[2]}")

    cursor.execute("""
        SELECT silos_armazenamento.id, silos_armazenamento.localidade, silos_armazenamento.capacidade, cooperativas_mae.nome_cooperativa 
        FROM silos_armazenamento 
        JOIN cooperativas_mae ON silos_armazenamento.id_cooperativa = cooperativas_mae.id
    """)

    silos = cursor.fetchall()

    if silos:
        print("\n--- SILOS ---")
        for silo in silos:
            print(f"ID: {silo[0]} | Localidade: {silo[1]} | Capacidade: {silo[2]}t | Coop: {silo[3]}")
    else:
        print("\nNenhum silo cadastrado.")


def deletar_cooperativa():
    try:
        print("\n" + "=" * 40)
        print(" DELETAR COOPERATIVA MÃE ")
        print("=" * 40)

        cursor.execute("SELECT id, nome_cooperativa FROM cooperativas_mae")
        coops = cursor.fetchall()
        
        if not coops:
            print("\n Nenhuma cooperativa cadastrada no sistema.")
            return

        print("Cooperativas cadastradas:")
        for coop in coops:
            print(f"ID: {coop[0]} | Nome: {coop[1]}")

        id_cooperativa = int(input("\nDigite o ID da cooperativa que deseja deletar: "))

        cursor.execute("DELETE FROM silos_armazenamento WHERE id_cooperativa = ?", (id_cooperativa,))
        cursor.execute("DELETE FROM cooperativas_mae WHERE id = ?", (id_cooperativa,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("\n Cooperativa e seus silos vinculados foram deletados com sucesso!")
        else:
            print("\n Nenhum registro encontrado com o ID informado.")

    except ValueError:
        print("\nErro: O ID deve ser um número inteiro válido.")
    except sqlite3.Error as e:
        print(f"\nErro ao deletar cooperativa: {e}")


def atualizar_cooperativa():
    try:
        print("\n" + "=" * 40)
        print(" ATUALIZAR COOPERATIVA MÃE ")
        print("=" * 40)

        cursor.execute("SELECT id, nome_cooperativa, registro_ocb FROM cooperativas_mae")
        coops = cursor.fetchall()
        
        if not coops:
            print("\nNenhuma cooperativa cadastrada no sistema.")
            return

        print("Cooperativas cadastradas:")
        for coop in coops:
            print(f"ID: {coop[0]} | Nome: {coop[1]} | OCB: {coop[2]}")

        id_cooperativa = int(input("\n Digite o ID da cooperativa que deseja atualizar: "))

        cursor.execute("SELECT id FROM cooperativas_mae WHERE id = ?", (id_cooperativa,))
        if not cursor.fetchone():
            print("\n Nenhum registro encontrado com o ID informado.")
            return

        novo_nome = input("Novo nome da cooperativa: ")
        novo_ocb = input("Novo registro OCB: ")

        cursor.execute(
            """
            UPDATE cooperativas_mae 
            SET nome_cooperativa = ?, registro_ocb = ? 
            WHERE id = ?
            """,
            (novo_nome, novo_ocb, id_cooperativa)
        )
        conexao.commit()
        print("\n Cooperativa atualizada com sucesso!")

    except ValueError:
        print("\n Erro: O ID deve ser um número inteiro válido.")
    except sqlite3.Error as e:
        print(f"\n Erro ao atualizar cooperativa: {e}")


def menu():
    criar_tabelas_cooperativas()
    
    while True:
        print("\n" + "=" * 40)
        print(" MENU PRINCIPAL ")
        print("=" * 40)
        print("1| Cadastrar Cooperativa")
        print("2| Cadastrar Silos")
        print("3| Listar Dados")
        print("4| Atualizar Cooperativa")
        print("5| Deletar Cooperativa")
        print("6| Sair")

        opcao = input("\nEscolha a opção: ")

        if opcao == "1":
            cadastrar_cooperativa()
        elif opcao == "2":
            cadastrar_silos()
        elif opcao == "3":
            listar_dados()
        elif opcao == "4":
            atualizar_cooperativa()
        elif opcao == "5":
            deletar_cooperativa()
        elif opcao == "6":
            print("\n Saindo do menu...")
            break
        else:
            print("\n Opção errada, tente novamente! ")

menu()
conexao.close()