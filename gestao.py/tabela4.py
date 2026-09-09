from banco import conectar
import sqlite3


def cadastrar_aluno():
    try:
        print("\n ----CADASTRO ALUNO----")
        nome = input("digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        id_turmas = input("Digite o ID da turma vinculada: ")


        assert nome != "", "O nome do aluno nao pode estar vazio"
        assert idade >= 3 "A), "A idade do aluno deve ser igual ou superior a 3 anos."
    assert id_turma > 0, "O ID da turma deve ser maior que zero."

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?)",
        (nome, idade, id_turma),
    )
    conexao.commit()
    conexao.close()
    print("Aluno cadastrado com sucesso!")

  except ValueError:
    print("Erro: Idade e ID da turma devem ser números inteiros.")
  except AssertionError as e:
    print(f"Erro de validação: {e}")
  except sqlite3.Error as e:
    print(
        "Erro no banco de dados: A turma informada provavelmente não existe."
        f" Detalhes: {e}"
    )


def listar_alunos():
  try:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
            SELECT alunos.id, alunos.nome, alunos.idade, turmas.nome_turma 
            FROM alunos 
            JOIN turmas ON alunos.id_turma = turmas.id
        """)
    alunos = cursor.fetchall()
    conexao.close()

    print("\n--- LISTA DE ALUNOS ---")
    if not alunos:
      print("Nenhum aluno cadastrado.")
    else:
      for aluno in alunos:
        print(
            f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} anos | Turma:"
            f" {aluno[3]}"
        )
  except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")


def alterar_aluno():
  try:
    listar_alunos()
    id_aluno = int(input("Digite o ID do aluno que deseja alterar: ").strip())
    novo_nome = input("Digite o novo nome: ").strip()
    nova_idade = int(input("Digite a nova idade: ").strip())
    id_turma = int(input("Digite o novo ID da turma: ").strip())

    assert novo_nome != "", "O nome não pode ser vazio."
    assert nova_idade >= 3, "A idade deve ser igual ou superior a 3 anos."
    assert id_turma > 0, "O ID da turma deve ser maior que zero."

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE alunos SET nome = ?, idade = ?, id_turma = ? WHERE id = ?",
        (novo_nome, nova_idade, id_turma, id_aluno),
    )
    conexao.commit()
    conexao.close()
    print("Aluno atualizado com sucesso!")

  except ValueError:
    print("Erro: Digite valores numéricos válidos para idade, ID ou turma.")
  except AssertionError as e:
    print(f"Erro de validação: {e}")
  except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")


def excluir_aluno():
  try:
    listar_alunos()
    id_aluno = int(input("Digite o ID do aluno que deseja excluir: ").strip())

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
    conexao.commit()
    conexao.close()
    print("Aluno excluído com sucesso!")

  except ValueError:
    print("Erro: Digite um valor numérico válido para o ID.")
  except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}") "
