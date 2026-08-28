silos = []

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
