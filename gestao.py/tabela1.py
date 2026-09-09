from banco import conectar
import sqlite3


def cadastrar_escola():
    try:
        print("\n -----CADASTRAR ESCOLAS-----")
        nome = input("Digite o nome da escola: ")
        cidade = input("Digite a cidade onde a escola fica: ")


        assert nome != "", "O nome da escola nao pode estar vazio"
        assert cidade != "", "O nome da cidade nao pode estar vazio"

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUE (?, ?)", (nome_cidade, nome_escola)
        )
        conexao.commit()
        conexao.close()
        print("Escola cadastrada com sucesso: ")

    except AssertionERROR as e:
        print(f"Erro de validação: {e}")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")


def listar_escolas():
    try
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()
        conexao.close()

        print("\n --- LISTAR ESCOLAS ---")
        if not escolas:
            print("Nenhuma escolas cadastrada")
        else:
            for escolas in escolas:
                print(f"ID: {escola[0]} | nome: {escola[1]} | cidade: {escolas[2]}")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

def alterar_escola():
    try:
        listar_escolas()
        id_escola = int(
            input("Digite o ID da escola que voce queira alterar: ")
        )

    novo_nome = input("Digite o novo nome da escola: ")
    nova_cidade = input("Digite o novo nome da escola: ")

    assert novo_nome != "", "O novo nome nao pode estar vazio"
    assert nova_cidade != "", "A nova cidadade nao pode estar vazio"

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE escolas SET nome  = ?, cidade = ? WHERE id = ?",
        (novo_nome, nova_cidad, id_escola),
    )
    conexao.commit()
    conexao.close()
    print("Escola atualizada com sucesso! ")

    except ValueError:
        print("Erro: Digite um valor numerico valido para o ID: ")
    except AssertionError as e:
        print(f"Erro de validação: {e}")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")


def excluir_escola():
  try:
    listar_escolas()
    id_escola = int(input("Digite o ID da escola que deseja excluir: ").strip())

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,))
    conexao.commit()
    conexao.close()
    print("Escola excluída com sucesso!")

  except ValueError:
    print("Erro: Digite um valor numérico válido para o ID.")
  except sqlite3.Error as e:
    print(
        f"Erro no banco de dados (certifique-se de que não há turmas"
        f" vinculadas): {e}"
    )