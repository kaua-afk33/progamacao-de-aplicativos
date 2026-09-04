import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def exibir_menu():
    print("\n--- SISTEMA DE LABORATÓRIO (SQLite) ---")
    print("1. Cadastrar Agendamento")
    print("2. Listar Agendamentos")
    print("3. Atualizar Agendamento")
    print("4. Deletar Agendamento")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ")

def cadastrar():
    print("\n--- NOVO CADASTRO ---")
    
    nome = input("Nome do solicitante: ")
    if not nome:
        print("Erro: O nome não pode estar vazio.")
        return

    data = input("Data (ex: 10/10/2026): ")
    if not data:
        print("Erro: A data não pode estar vazia.")
        return

    horario = input("Horário (ex: 14:30): ")
    if not horario:
        print("Erro: O horário não pode estar vazio.")
        return

    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM agendamentos WHERE data = ? AND horario = ?",
        (data, horario)
    )
    if cursor.fetchone():
        print("Erro: Este horário não está disponível para esta data.")
        conexao.close()
        return

    cursor.execute(
        "INSERT INTO agendamentos (nome, data, horario) VALUES (?, ?, ?)",
        (nome, data, horario)
    )
    conexao.commit()
    conexao.close()

    print(f"Sucesso: Agendamento para {nome} em {data} às {horario} salvo no banco de dados!")

def listar():
    print("\n--- AGENDAMENTOS CADASTRADOS ---")
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, data, horario FROM agendamentos")
    resultados = cursor.fetchall()
    conexao.close()

    if not resultados:
        print("Nenhum agendamento encontrado no banco de dados.")
    else:
        for row in resultados:
            id_ag, nome, data, horario = row
            print(f"ID [{id_ag}] | Solicitante: {nome} | Data: {data} | Horário: {horario}")

def atualizar():
    print("\n--- ATUALIZAR AGENDAMENTO ---")
    listar()
    
    id_ag = input("Digite o ID do agendamento que deseja atualizar: ")

    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM agendamentos WHERE id = ?", (id_ag,))
    if not cursor.fetchone():
        print("Erro: Agendamento não encontrado.")
        conexao.close()
        return

    nome = input("Novo nome do solicitante: ")
    if not nome:
        print("Erro: O nome não pode estar vazio.")
        conexao.close()
        return

    data = input("Nova data: ")
    if not data:
        print("Erro: A data não pode estar vazia.")
        conexao.close()
        return

    horario = input("Novo horário: ")
    if not horario:
        print("Erro: O horário não pode estar vazio.")
        conexao.close()
        return

    cursor.execute(
        "SELECT id FROM agendamentos WHERE data = ? AND horario = ? AND id != ?",
        (data, horario, id_ag)
    )
    if cursor.fetchone():
        print("Erro: Este horário não está disponível para esta data.")
        conexao.close()
        return

    cursor.execute(
        "UPDATE agendamentos SET nome = ?, data = ?, horario = ? WHERE id = ?",
        (nome, data, horario, id_ag)
    )
    conexao.commit()
    conexao.close()
    print(f"Sucesso: Agendamento ID {id_ag} atualizado!")

def deletar():
    print("\n--- DELETAR AGENDAMENTO ---")
    listar()
    
    id_ag = input("Digite o ID do agendamento que deseja deletar: ")

    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM agendamentos WHERE id = ?", (id_ag,))
    if not cursor.fetchone():
        print("Erro: Agendamento não encontrado.")
        conexao.close()
        return

    cursor.execute("DELETE FROM agendamentos WHERE id = ?", (id_ag,))
    conexao.commit()
    conexao.close()
    print(f"Sucesso: Agendamento ID {id_ag} deletado!")

def main():
    inicializar_banco()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha entre 1 e 5.")

if __name__ == "__main__":
    main()