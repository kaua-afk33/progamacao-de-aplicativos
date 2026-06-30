import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db') #o aluno tenta cadastrar uma serie com id_escola = 999 (que não existe)
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome_serie, id_escola))#o SQLite aceia o cadastro mesmo assim. oq esta faltando ativar?
        conexao.commit()
    execept sqlite3.IntegrityError: 
        print("Erro: Escola Inexistente!")
    finally:
        conexao.close()


