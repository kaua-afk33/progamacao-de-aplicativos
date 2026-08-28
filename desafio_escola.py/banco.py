import sqlite3

conexao = sqlite3.connect("gestao_escolar.db")
cursor = conexao.cursor()

def criar_tabelas():
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREAT TABLE IF NOT EXIST gestao_escolar.db(
            id INTEGER PRIMARY KEY AUTOCREMENT,
            escola TEXT NOT NULL,
            quandidade_de_alunos NOT NULL,
            id_escola INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREAT TABLE IF NOT EXIST turmas(
            id INTEGER PRIMARY KEY AUTOCREMENT,
            turmas INTEGER NOT NULL,
            id_turmas INTEGER NOT NULL,
            FOREING KEY (id_gestao_escolar_db) REFERENCES gestao_escolar.db(id)
        )
    ''')

    cursor.execute('''
        CREAT TABLE IF NOT EXIST alunos(
            id INTEGER PRIMARY KEY AUTOCREMENT,
            nome_alunos TEXT NOT NULL,
            idade INTEGER NOT NULL,
            id_aluno INTEGER NOT NULL,
            FOREING KEY (id_gestao_escolar.db) REFERENCES gestao_escolar.db(id)
        )
    ''')

