import sqlite3 
id_prof = int(input("Digite o id do professor: "))
def buscar_professor(id_prof): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()

    cursor.execute(f"SELECT nome FROM professores WHERE id = {id_prof}") 
    resultado = cursor.fetchone() 
    print(resultado) 
    conexao.close() 

buscar_professor(id_prof)

# id_prof no Python cria apenas uma variável entre parênteses, e não uma tupla. O SQLite exige obrigatoriamente uma tupla para passar parâmetros.