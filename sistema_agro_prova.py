import sqlite3

conexao = sqlite3.connect("cooperativa_agricola.db")
cursor = conexao.cursor()


def criar_tabelas_cooperativas():
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cooperativas_mae (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cooperativa TEXT NOT NULL,
            registro_ocb TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS silos_armazenamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            localidade TEXT NOT NULL,
            capacidade INTEGER NOT NULL,
            id_cooperativa INTEGER NOT NULL,
            FOREIGN KEY (id_cooperativa) REFERENCES cooperativas_mae(id)
        )
    ''')

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
        print("\nCooperativa cadastrada com sucesso!")
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
        print("\nSilo cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: O ID da cooperativa mãe informado não existe no sistema.")
    except ValueError:
        print("Erro: A capacidade e o ID devem ser números inteiros.")


def listar_dados():
    print("\n" + "=" * 40)
    print(" RELATÓRIO GERAL: COOPERATIVAS E SILOS ")
    print("=" * 40)

    cursor.execute("""
        SELECT c.id, c.nome_cooperativa, c.registro_ocb, s.id, s.localidade, s.capacidade 
        FROM cooperativas_mae c 
        LEFT JOIN silos_armazenamento s ON c.id = s.id_cooperativa
    """)

    resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum registro encontrado no banco de dados.")
        return

    cooperativa_atual = None
    for linha in resultados:
        id_coope, nome_coope, reg_ocb, id_silo, localidade, capacidade = linha

        if cooperativa_atual != id_coope:
            cooperativa_atual = id_coope
            print(f"\n[Cooperativa ID: {id_coope}] Nome: {nome_coope} | OCB: {reg_ocb}")
            print("   Silos Vinculados:")

        if id_silo is not None:
            print(f"Silo ID: {id_silo} | Localidade: {localidade} | Capacidade: {capacidade}t")
        else:
            print("     (Nenhum silo cadastrado para esta cooperativa)")


def listar_silos():
    print("\n" + "=" * 40)
    print(" RELATÓRIO: APENAS SILOS ")
    print("=" * 40)

    cursor.execute("""
        SELECT s.id, s.localidade, s.capacidade, c.nome_cooperativa 
        FROM silos_armazenamento s
        JOIN cooperativas_mae c ON s.id_cooperativa = c.id
    """)
    silos = cursor.fetchall()

    if not silos:
        print("\nNenhum silo cadastrado no sistema.")
        return

    print("\n--- SILOS ---")
    for silo in silos:
        print(f"ID: {silo[0]} | Localidade: {silo[1]} | Capacidade: {silo[2]}t | Coop: {silo[3]}")


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

        id_cooperativa = int(input("\nDigite o ID da cooperativa que deseja atualizar: "))

        cursor.execute("SELECT id FROM cooperativas_mae WHERE id = ?", (id_cooperativa,))
        if not cursor.fetchone():
            print("\nNenhum registro encontrado com o ID informado.")
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
        print("\nCooperativa atualizada com sucesso!")

    except ValueError:
        print("\nErro: O ID deve ser um número inteiro válido.")
    except sqlite3.Error as e:
        print(f"\nErro ao atualizar cooperativa: {e}")


def atualizar_silos():
    try:
        print("\n" + "=" * 40)
        print(" ATUALIZAR SILO ")
        print("=" * 40)

        cursor.execute("""
            SELECT s.id, s.localidade, s.capacidade, c.nome_cooperativa 
            FROM silos_armazenamento s
            JOIN cooperativas_mae c ON s.id_cooperativa = c.id
        """)
        silos = cursor.fetchall()
        
        if not silos:
            print("\nNenhum silo cadastrado no sistema.")
            return

        print("Silos cadastrados:")
        for silo in silos:
            print(f"ID: {silo[0]} | Localidade: {silo[1]} | Capacidade: {silo[2]}t | Coop: {silo[3]}")

        id_silo = int(input("\n Digite o ID do silo que deseja atualizar: "))

        cursor.execute("SELECT id FROM silos_armazenamento WHERE id = ?", (id_silo,))
        if not cursor.fetchone():
            print("\nNenhum silo encontrado com o ID informado.")
            return

        nova_localidade = input("Nova localidade do silo: ")
        nova_capacidade = int(input("Nova capacidade do silo [toneladas]: "))
        novo_id_coop = int(input("Novo ID da cooperativa mãe vinculada: "))

        cursor.execute(
            """
            UPDATE silos_armazenamento 
            SET localidade = ?, capacidade = ?, id_cooperativa = ? 
            WHERE id = ?
            """,
            (nova_localidade, nova_capacidade, novo_id_coop, id_silo)
        )
        conexao.commit()
        print("\nSilo atualizado com sucesso!")

    except ValueError:
        print("\nErro: Capacidade e IDs devem ser números inteiros válidos.")
    except sqlite3.IntegrityError:
        print("\nErro: O ID da cooperativa mãe informado não existe no sistema.")
    except sqlite3.Error as e:
        print(f"\nErro ao atualizar silo: {e}")


def deletar_cooperativa():
    try:
        print("\n" + "=" * 40)
        print(" DELETAR COOPERATIVA MÃE ")
        print("=" * 40)

        cursor.execute("SELECT id, nome_cooperativa FROM cooperativas_mae")
        coops = cursor.fetchall()
        
        if not coops:
            print("\nNenhuma cooperativa cadastrada no sistema.")
            return

        print("Cooperativas cadastradas:")
        for coop in coops:
            print(f"ID: {coop[0]} | Nome: {coop[1]}")

        id_cooperativa = int(input("\nDigite o ID da cooperativa que deseja deletar: "))

        cursor.execute("DELETE FROM silos_armazenamento WHERE id_cooperativa = ?", (id_cooperativa,))
        cursor.execute("DELETE FROM cooperativas_mae WHERE id = ?", (id_cooperativa,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("\nCooperativa e seus silos vinculados foram deletados com sucesso!")
        else:
            print("\nNenhum registro encontrado com o ID informado.")

    except ValueError:
        print("\nErro: O ID deve ser um número inteiro válido.")
    except sqlite3.Error as e:
        print(f"\nErro ao deletar cooperativa: {e}")


def deletar_silos():
    try:
        print("\n" + "=" * 40)
        print(" DELETAR SILO ")
        print("=" * 40)

        cursor.execute("""
            SELECT s.id, s.localidade, s.capacidade, c.nome_cooperativa 
            FROM silos_armazenamento s
            JOIN cooperativas_mae c ON s.id_cooperativa = c.id
        """)
        silos = cursor.fetchall()
        
        if not silos:
            print("\nNenhum silo cadastrado no sistema.")
            return

        print("Silos cadastrados:")
        for silo in silos:
            print(f"ID: {silo[0]} | Localidade: {silo[1]} | Capacidade: {silo[2]}t | Coop: {silo[3]}")

        id_silo = int(input("\nDigite o ID do silo que deseja deletar: "))

        cursor.execute("DELETE FROM silos_armazenamento WHERE id = ?", (id_silo,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("\nSilo deletado com sucesso!")
        else:
            print("\nNenhum silo encontrado com o ID informado.")

    except ValueError:
        print("\nErro: O ID deve ser um número inteiro válido.")
    except sqlite3.Error as e:
        print(f"\nErro ao deletar silo: {e}")


def menu():
    criar_tabelas_cooperativas()
   
    while True:
        print("\n" + "=" * 40)
        print(" MENU PRINCIPAL ")
        print("=" * 40)
        print("1| Cadastrar Cooperativa")
        print("2| Cadastrar Silos")
        print("3| Listar Geral (Cooperativas e Silos)")
        print("4| Listar Apenas Silos")
        print("5| Atualizar Cooperativa")
        print("6| Atualizar Silo")
        print("7| Deletar Cooperativa")
        print("8| Deletar Silo")
        print("9| Sair")

        opcao = input("\nEscolha a opção: ")

        if opcao == "1":
            cadastrar_cooperativa()
        elif opcao == "2":
            cadastrar_silos()
        elif opcao == "3":
            listar_dados()
        elif opcao == "4":
            listar_silos()
        elif opcao == "5":
            atualizar_cooperativa()
        elif opcao == "6":
            atualizar_silos()
        elif opcao == "7":
            deletar_cooperativa()
        elif opcao == "8":
            deletar_silos()
        elif opcao == "9":
            print("\nSaindo do menu...")
            break
        else:
            print("\nOpção inválida, tente novamente!")

menu()
conexao.close()