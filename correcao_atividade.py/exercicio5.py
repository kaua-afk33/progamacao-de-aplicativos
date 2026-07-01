import sqlite3

def vincular_aluno():
    nome = input("Nome do aluno: ")
    
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))
        
        # Conectando ao banco de dados
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        
        # Inserindo o aluno
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
        print("Aluno vinculado com sucesso!")
        
    except ValueError:
        # Trata o erro caso o usuário digite texto em vez de um número no ID
        print("Erro: O ID da turma precisa ser um número inteiro.")
        
    except sqlite3.Error as erro:
        # Trata os erros específicos do SQLite
        print(f"Erro no banco de dados: {erro}")
        
    finally:
        # O bloco finally garante que a conexão fecha, mas só se ela tiver sido aberta
        if 'conexao' in locals():
            conexao.close()

# Para testar a função:
vincular_aluno()