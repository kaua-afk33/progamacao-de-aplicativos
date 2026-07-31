import sqlite3 
 
def deletar_escola_antiga(): 
    id_escola = int(input("ID da escola a remover: ")) 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
    
    cursor.execute(f"DELETE FROM escolas WHERE id = {id_escola}") 
     
    conexao.commit() 
    conexao.close() 
deletar_escola_antiga()

# O comando SQL comparou o campo da tabela com o próprio nome da variável Python como texto estático, em vez de passar o seu valor.