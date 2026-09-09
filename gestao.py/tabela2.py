from banco import conectar
import sqlite3


def cadastrar_turma():
  try:
    print("\n--- CADASTRO DE TURMA ---")
    nome_turma = input("Digite o nome da turma: ").strip()
    id_escola_str = input("Digite o ID da escola vinculada: ").strip()

    id_escola = int(id_escola_str)

    assert nome_turma != "", "O nome da turma não pode ser vazio."
    assert id_escola > 0, "O ID da escola deve ser maior que zero."

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)",
        (nome_turma, id_escola),
    )
    conexao.commit()
    conexao.close()
    print("Turma cadastrada com sucesso!")

  except ValueError:
    print("Erro: O ID da escola deve ser um número inteiro.")
  except AssertionError as e:
    print(f"Erro de validação: {e}")
  except sqlite3.Error as e:
    print(
        "Erro no banco de dados: A escola informada provavelmente não existe."
        f" Detalhes: {e}"
    )


def listar_turmas():
  try:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
            SELECT turmas.id, turmas.nome_turma, escolas.nome 
            FROM turmas 
            JOIN escolas ON turmas.id_escola = escolas.id
        """)
    turmas = cursor.fetchall()
    conexao.close()

    print("\n--- LISTA DE TURMAS ---")
    if not turmas:
      print("Nenhuma turma cadastrada.")
    else:
      for turma in turmas:
        print(
            f"ID Turma: {turma[0]} | Turma: {turma[1]} | Escola Vinculada:"
            f" {turma[2]}"
        )
  except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")


def alterar_turma():
  try:
    listar_turmas()
    id_turma = int(input("Digite o ID da turma que deseja alterar: ").strip())
    novo_nome = input("Digite o novo nome da turma: ").strip()
    id_escola = int(input("Digite o novo ID da escola vinculada: ").strip())

    assert novo_nome != "", "O nome da turma não pode ser vazio."
    assert id_escola > 0, "O ID da escola deve ser maior que zero."

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE turmas SET nome_turma = ?, id_escola = ? WHERE id = ?",
        (novo_nome, id_escola, id_turma),
    )
    conexao.commit()
    conexao.close()
    print("Turma atualizada com sucesso!")

  except ValueError:
    print("Erro: Digite valores numéricos válidos para os IDs.")
  except AssertionError as e:
    print(f"Erro de validação: {e}")
  except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")


def excluir_turma():
  try:
    listar_turmas()
    id_turma = int(input("Digite o ID da turma que deseja excluir: ").strip())

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM turmas WHERE id = ?", (id_turma,))
    conexao.commit()
    conexao.close()
    print("Turma excluída com sucesso!")

  except ValueError:
    print("Erro: Digite um valor numérico válido para o ID.")
  except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")