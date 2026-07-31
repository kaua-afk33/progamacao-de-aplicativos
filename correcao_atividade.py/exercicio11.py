import sqlite3 
 
def listar_alunos_e_turmas(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas ON alunos.id_turma = turmas.id") 
     
    for linha in cursor.fetchall(): 
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}") 
    conexao.close() 

# Foi feito um INNER JOIN sem especificar a cláusula de ligação ON. Isso faz o banco multiplicar todas as linhas de uma tabela pelas da outra Produto Cartesiano.