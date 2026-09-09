turmas = []

def tabelas():
    cursor.execute("PRAGMA  foreign_keys = ON")

    cursor.execute('''
        CREAT TABLE IF NOT EXIST gestao_escolar(
            id INTEGER PRYMARI KEY AUTOCREMENT,
            nome_cidade TEXT NOT NULL,
            
    )
''')

    cursor.execute('''
        CREAT TABLE IF NOT EXIST escola(
            id INTEGER PRYMARI KEY AUTOCREMENT,
            nome_escola TEXT NOT NULL,
            id_escola INTEGER NOT NULL,
            FOREING KEY (id_escola) REFERENCE escolas(id)
        )
    ''')    

    cursor.execute('''
        CREAT TABLE IF NOT EXIST turmas(
            id INTEGER PRYMARI KEY AUTOCREMENT,
            nome_turma TEXT NOT NUL,
            quantidade_turmas TEXT NOT NULL,
            FOREING KEY (id_turma) REFERENCES turmas(id)
        )
    ''')

    cursor.execute('''
        CREAT TABLE IF NOT EXIST aluno(
            id INTEGER PRYMARI KEY AUTOCREMENT,
            nome_aluno TEXT NOT NULL,
            idade_aluno TEXT NOT NULL,
        )
    ''')

    conexao.commit()
    conexao.close()

    criar_tabelas()
    print("tabela de dados criado com sucesso: ")