import sqlite3

def conectar_e_consultar():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    
    print("Conexão com o banco de dados 'sistema_escola.db' realizada com sucesso!\n")
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    
    print("Tabelas encontradas no banco de dados:")
    for tabela in tabelas:
        print(f"- {tabela[0]}")
        
    conexao.close()

if __name__ == "__main__":
    conectar_e_consultar()