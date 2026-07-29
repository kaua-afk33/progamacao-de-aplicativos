import sqlite3 

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
             (nome_serie, id_escola)
        )

        conexao.commit()
        print("serie cadastrada com sucesso")

    except sqlite3.IntegrityError: 
        print("Erro: Escola Inexistente!")

    finally:
        conexao.close()


cadastrar_serie("2º ano do ensino medio", 1)