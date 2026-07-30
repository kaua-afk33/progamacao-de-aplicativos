import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')


    conexao.commit()
    cursor.execute(
        "SELECT nome FROM professores WHERE id = ?",
        (id_prof,)
    )


    resultado = cursor.fetchone()

    if resultado:
        print("Professor encontrado:", resultado[0])
    else:
        print("Professor não encontrado!")

    conexao.close()

buscar_professor(1)   