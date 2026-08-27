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
            print("   Silos Vinculados:")

        if id_silo is not None:
            print(f"Silo ID: {id_silo} | Localidade: {localidade} | Capacidade: {capacidade}t")
        else:
            print("     (Nenhum silo cadastrado para esta cooperativa)")


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

