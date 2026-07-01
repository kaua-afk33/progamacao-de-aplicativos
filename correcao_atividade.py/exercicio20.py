
import sqlite3

def cadastrar_escola_manual():
    # O aluno resolveu gerar o ID por conta própria
    try:
        id_escola = int(input("Digite o ID para a nova escola: "))
    except ValueError:
        print("Erro: O ID precisa ser um número inteiro!")
        return

    nome = input("Nome da escola: ")

    # Boa prática: Usar o 'with' garante que a conexão feche mesmo se ocorrer um erro
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        # A blindagem protetora contra IDs duplicados acontece aqui:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )

        conexao.commit()
        print(f"Escola '{nome}' cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        # Captura especificamente o erro de ID duplicado (Primary Key violation)
        print(f"Erro: Já existe uma escola cadastrada com o ID {id_escola}. Tente outro.")
    
    except sqlite3.Error as e:
        # Captura qualquer outro erro genérico do banco de dados
        print(f"Ocorreu um erro no banco de dados: {e}")
        
    finally:
        # Garante que a conexão seja fechada independente de ter dado erro ou não
        if conexao:
            conexao.close()

# Para testar a função
# cadastrar_escola_manual()