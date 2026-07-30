import sqlite3

def vincular_aluno():
    nome = input("Nome do aluno: ")
    
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
        print("Aluno vinculado com sucesso!")
        
    except ValueError:
        print("Erro: O ID da turma precisa ser um número inteiro.")
        
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
        
    finally:
        if 'conexao' in locals():
            conexao.close()

vincular_aluno()