import sqlite3 
 
def verificar_registros(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute("SELECT * FROM alunos") 
     
    print("Primeiro print:", cursor.fetchall()) 


    cursor.execute("SELECT * FROM alunos") 
    print("Segundo print:", cursor.fetchall()) 
     
    conexao.close() 

verificar_registros()

# cursor.fetchall() funciona como um leitor que consome os dados.