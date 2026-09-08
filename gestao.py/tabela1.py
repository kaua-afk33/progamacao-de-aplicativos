turmas = []

def tabelas():
    cursor.execute("PRAGMA  foreign_keys = ON")

    cursor.execute('''
        CREAT TABLE IF NOT EXIST gestao_escolar(
            id INTEGER PRYMARI KEY AUTOCREMENT,
            nome_escola TEXT NOT NULL,
            id_escola INTEGER NOT NULL
    )
''')

    
    cursor.execute('''
        CREAT TABLE IN NOT EXIST gestao_escolar(
            id INTEGER PRYMARI KEY AUTOCREMENT,
            nome_turma TEXT NOT NULL,
            quantidade_turma INTEGER NOT NULL,
            FOREIGN KEY (id_getao_escolar) REFERENCE gestao_mae(id)
        )
    ''')


    cursor.execute('''
        CREAT TABLE IF NOT EXIST gestao_escolar(
            id INTEGER PRYMARI KEY AUTOCREMENT,
            nome_aluno TEXT NOT NULL,
            id_aluno INTEGER NOT NULL,
            FOREIGN KEY (id_getao_escolar) REFERENCE gestao_mae(id)
        )
    ''')
    