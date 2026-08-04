import sqlite3


def criar_tabelas():
  try:
    with sqlite3.connect("hospital.db") as conexao:
      cursor = conexao.cursor()
      cursor.execute("PRAGMA foreign_keys = ON;")

      cursor.execute("""
                CREATE TABLE IF NOT EXISTS hospitais (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cidade TEXT NOT NULL
                )
            """)

      cursor.execute("""
                CREATE TABLE IF NOT EXISTS medicos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    crm TEXT NOT NULL,
                    id_hospital INTEGER NOT NULL,
                    FOREIGN KEY (id_hospital) REFERENCES hospitais (id)
                )
            """)
      conexao.commit()
    print("Banco de dados e tabelas verificados/criados com sucesso!")
  except sqlite3.Error as e:
    print(f"Erro no banco de dados ao criar as tabelas: {e}")


def cadastrar_hospital():
  try:
    nome = input("Digite o nome do hospital: ")
    cidade = input("Digite a cidade do hospital: ")

    if not nome.strip() or not cidade.strip():
      print("Erro: O nome e a cidade do hospital não podem estar vazios.")
      return

    with sqlite3.connect("hospital.db") as conexao:
      cursor = conexao.cursor()
      cursor.execute("PRAGMA foreign_keys = ON;")
      cursor.execute(
          "INSERT INTO hospitais (nome, cidade) VALUES (?, ?)", (nome, cidade)
      )
      conexao.commit()

    print("Hospital cadastrado com sucesso no banco de dados!")
  except sqlite3.Error as e:
    print(f"Erro do SQLite ao cadastrar hospital: {e}")
  except Exception as e:
    print(f"Erro inesperado no cadastro: {e}")


def listar_hospitais():
  try:
    with sqlite3.connect("hospital.db") as conexao:
      cursor = conexao.cursor()
      cursor.execute("PRAGMA foreign_keys = ON;")
      cursor.execute("SELECT id, nome, cidade FROM hospitais")
      hospitais = cursor.fetchall()

    print("\n--- LISTA DE HOSPITAIS ---")
    if not hospitais:
      print("Nenhum hospital cadastrado no banco ainda.")
      return False

    for h in hospitais:
      print(f"ID: {h[0]} | Nome: {h[1]} | Cidade: {h[2]}")
    print("-" * 35)
    return True
  except sqlite3.Error as e:
    print(f"Erro ao listar hospitais: {e}")
    return False


def cadastrar_medico():
  try:
    tem_hospitais = listar_hospitais()
    if not tem_hospitais:
      print("Aviso: Cadastre um hospital primeiro antes de cadastrar médicos.")
      return

    nome = input("\nDigite o nome do médico: ")
    crm = input("Digite o CRM do médico: ")
    id_hospital_str = input("Digite o ID do hospital onde o médico atua: ")

    id_hospital = int(id_hospital_str)                                                    

    if not nome.strip() or not crm.strip():
      print("Erro: O nome e o CRM não podem estar vazios.")
      return

    with sqlite3.connect("hospital.db") as conexao:
      cursor = conexao.cursor()
      cursor.execute("PRAGMA foreign_keys = ON;")

      cursor.execute("SELECT id FROM hospitais WHERE id = ?", (id_hospital,))
      hospital_existe = cursor.fetchone()

      if not hospital_existe:
        print(f"Erro: O hospital com ID {id_hospital} não foi encontrado.")
        return

      cursor.execute(
          "INSERT INTO medicos (nome, crm, id_hospital) VALUES (?, ?, ?)",
          (nome, crm, id_hospital),
      )
      conexao.commit()

    print("Médico cadastrado e vinculado ao hospital com sucesso!")
  except ValueError:
    print("Erro: O ID do hospital deve ser um número inteiro válido.")
  except sqlite3.Error as e:
    print(f"Erro no banco de dados ao cadastrar médico: {e}")
  except Exception as e:
    print(f"Erro inesperado: {e}")


def menu():
  criar_tabelas()
  while True:
    print("\n--- MENU SISTEMA DE HOSPITAIS ---")
    print("1. Cadastrar Hospital")
    print("2. Listar Hospitais (Ver IDs)")
    print("3. Cadastrar Médico")
    print("0. Sair")

    try:
      opcao = int(input("Escolha uma opção: "))
      if opcao == 1:
        cadastrar_hospital()
      elif opcao == 2:
        listar_hospitais()
      elif opcao == 3:
        cadastrar_medico()
      elif opcao == 0:
        print("Saindo do programa...")
        break
      else:
        print("Opção inválida! Escolha entre 0 e 3.")
    except ValueError:
      print("Erro: Digite apenas números inteiros para a opção.")


if __name__ == "__main__":
  menu()