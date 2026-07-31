import sqlite3
 
def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
        (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()

serie = input("Digite o nome de uma série: ")
escola = int(input("Digite o id da escola: "))
cadastrar_serie(serie, escola)


# Foreign Keys desligada por questões de compatibilidade com versões antigas.