import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Correção 1: Coloquei as linhas para dentro da função (indentação)
    # Correção 2: Adicionei a vírgula após id_prof para transformá-lo em uma tupla: (id_prof,)
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    
    # Melhoria: Verifica se encontrou o professor antes de exibir
    if resultado:
        print(f"Professor encontrado: {resultado[0]}")
    else:
        print("Professor não encontrado.")
        
    conexao.close()

# Exemplo de como usar a função:
# buscar_professor(1)