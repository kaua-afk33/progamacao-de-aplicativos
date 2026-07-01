import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    try:
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUE (?, ?)",
(nome, id_escola))
    conexao.commit()
except sqlite3.Error as e:
    print("erro tecnico:", e)
finally:
    conexao.close()