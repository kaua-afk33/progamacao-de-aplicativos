import sqlite3

conexao = sqlite3.connect("sistema_academias.db")
cursor = conexao.cursor()

cursor.execute('''
    
CREATE TABLE IF NOT EXISTS academias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_unidade TEXT NOT NULL,
    bairro TEXT NOT NULL
 )

''')

cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    mensalidade REAL NOT NULL,
    id_academia INTEGER,
    FOREIGN KEY (id_academia) REFERENCES academias(id)
    )
'''
)

conexao.commit()

cursor.execute(
    """
INSERT INTO academias (nome_unidade, bairro) 
VALUES (?, ?)
""",
    ("Central Fitness", "Centro"),
)
academia_id = cursor.lastrowid 
conexao.commit()

alunos_para_inserir = [
    ("Caio D'Ávila", 120.50, academia_id),
    ("Maria Conceição", 150.00, academia_id),
    ("João-Pedro de Alcântara", 135.00, academia_id),
]

for nome, mensalidade, id_academia in alunos_para_inserir:
    cursor.execute(
        """
        INSERT INTO alunos (nome, mensalidade, id_academia) 
        VALUES (?, ?, ?)
    """,
        (nome, mensalidade, id_academia),
    )

conexao.commit()

print("--- Alunos Cadastrados com Sucesso ---")
cursor.execute("SELECT id, nome, mensalidade, id_academia FROM alunos")
for linha in cursor.fetchall():
    print(
        f"ID: {linha[0]} | Nome: {linha[1]} | Mensalidade: R$ {linha[2]} | ID Academia: {linha[3]}"
    )

conexao.close()