import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    
    except sqlite3.IntegrityError: 
        print("Erro: Este CPF já está cadastrado no sistema!") 

    except sqlite3.Error:
        print("Erro no codigo,")


    finally: 
        conexao.close() 

nome = input("Digite o nome do professor: ")
materia = input("Digite a materia do professor: ")
cpf = input("Digite o cpf do professor: ")
inserir_professor(nome, materia, cpf)

# O código usou um bloco except Genérico que capturava qualquer erro do banco, exibindo uma mensagem de "CPF Duplicado" mesmo quando o erro era na verdade uma palavra digitada errada no comando SQL.