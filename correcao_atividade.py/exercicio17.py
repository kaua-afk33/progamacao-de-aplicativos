import sqlite3

def inserir_professor(nome, materia, cpf):
    # Inicializamos a variável como None para o 'finally' não quebrar
    conexao = None
    try:
        conexao = sqlite3.connect("sistema_escola.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO professores (nome, materia, cpf) VALUES (?, ?, ?)",
            (nome, materia, cpf)
        )

        conexao.commit()
        print(f"Professor {nome} cadastrado com sucesso!")

    # Correção 1: Alinhamento (indentação) do except com o try
    except sqlite3.Error as e:
        # Exibe o erro real do banco para ajudar no diagnóstico
        print(f"Erro no banco de dados: {e}")

    # Correção 1: Alinhamento (indentação) do finally
    finally:
        # Correção 2: Só fecha a conexão se ela foi aberta com sucesso
        if conexao:
            conexao.close()

# Exemplo de uso:
# inserir_professor("Ana Costa", "Matemática", "111.222.333-44")