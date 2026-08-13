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
        "INSERT INTO cooperativas_mae (nome_cooperativa, registro_ocb) VALUES"
        " (?, ?)",
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
    id_cooperativa = int(
        input("Qual é o ID da cooperativa mãe vinculada?: ")
    )


    cursor.execute(
        "INSERT INTO silos_armazenamento (localidade, capacidade,"
        "id_cooperativa) VALUES (?, ?, ?)",
        (localidade, capacidade, id_cooperativa),
    )           
    conexao.commit()
    print("\n Silo cadastrado com sucesso!")
  except sqlite3.IntegrityError:
    print("ERRO: O ID da cooperativa mãe informado não existe no sistema.")
  except ValueError:
    print("Erro: A capacidade e o ID devem ser números inteiros.")


def listar_dados():
  print("\n" + "=" * 40)
  print(" RELATÓRIO: COOPERATIVAS E SILOS ")
  print("=" * 40)

  cursor.execute("""
        SELECT c.id, c.nome_cooperativa, c.registro_ocb, s.localidade, s.capacidade 
        FROM cooperativas_mae c 
        LEFT JOIN silos_armazenamento s ON c.id = s.id_cooperativa
    """)

  resultados = cursor.fetchall()

  if not resultados:
    print("Nenhum registro encontrado no banco de dados.")
    return

  cooperativa_atual = None
  for linha in resultados:
    id_coope, nome_coope, reg_ocb, localidade, capacidade = linha

    if cooperativa_atual != id_coope:
      cooperativa_atual = id_coope
      print(
          f"\n[Cooperativa ID: {id_coope}] Nome: {nome_coope} | Registro OCB:"
          f" {reg_ocb}"
      )
      print("Silos Vinculados:")

    if localidade is not None:
      print(f"      • Localidade: {localidade} | Capacidade: {capacidade} ton")

  print("\n" + "=" * 40)


criar_tabelas_cooperativas()
cadastrar_cooperativa()
cadastrar_silos()
listar_dados()

conexao.close()