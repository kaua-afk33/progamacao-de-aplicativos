import sqlite3
def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)",(nome, id_serie, id_prof))
        conexao.commit()
    except sqlite3.OperationalError:
        print("Id professor nao existe.")
    
    finally:
        conexao.close()


nome = input("Digite o nome")
id_serie = int(input("Digite o id da serie: "))
id_prof = int(input("Digite o id do professor: "))
cadastrar_turma(nome, id_serie, id_prof)

# O comando conexao.close foi colocado ao final do script sem tratamento de exceções. Se houver qualquer erro no meio da execução, o programa para antes de fechar o banco.