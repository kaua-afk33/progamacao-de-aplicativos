import gestao_escolar
from banco import criar_tabelas
import escola
import turma


def menu():
  criar_tabelas()

  while True:
    print("\n==============================")
    print("    SISTEMA DE GESTÃO ESCOLAR ")
    print("==============================")
    print("--- MENU ESCOLAS ---")
    print("1. Cadastrar Escola")
    print("2. Listar Escolas")
    print("3. Alterar Escola")
    print("4. Excluir Escola")
    print("\n--- MENU TURMAS ---")
    print("5. Cadastrar Turma")
    print("6. Listar Turmas")
    print("7. Alterar Turma")
    print("8. Excluir Turma")
    print("\n--- MENU ALUNOS ---")
    print("9. Cadastrar Aluno")
    print("10. Listar Alunos")
    print("11. Alterar Aluno")
    print("12. Excluir Aluno")
    print("\n0. Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
      escola.cadastrar_escola()
    elif opcao == "2":
      escola.listar_escolas()
    elif opcao == "3":
      escola.alterar_escola()
    elif opcao == "4":
      escola.excluir_escola()
    elif opcao == "5":
      turma.cadastrar_turma()
    elif opcao == "6":
      turma.listar_turmas()
    elif opcao == "7":
      turma.alterar_turma()
    elif opcao == "8":
      turma.excluir_turma()
    elif opcao == "9":
      aluno.cadastrar_aluno()
    elif opcao == "10":
      aluno.listar_alunos()
    elif opcao == "11":
      aluno.alterar_aluno()
    elif opcao == "12":
      aluno.excluir_aluno()
    elif opcao == "0":
      print("Saindo do sistema... Até mais!")
      break
    else:
      print("Opção inválida! Escolha um número entre 0 e 12.")


menu()
conexao.close()