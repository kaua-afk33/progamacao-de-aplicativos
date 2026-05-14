2
open('habito.txt', 'w').close()

def criar():
    nome = input("Nome do habito: ")
    with open('habito.txt', 'a') as f:
        f.write(nome + '\n')
    print("Aluno cadastrado!")

def ler():
    with open('habito.txt', 'r') as f:
        alunos = f.readlines()
        i = 0
        for aluno in alunos:
            print(f"{i} - {aluno.strip()}")
            i += 1

def atualizar():
    ler() 
    idx = int(input("Digite o ID do habito que deseja alterar: "))
    novo_nome = input("Novo nome: ")
    
    with open('habito.txt', 'r') as f:
        linhas = f.readlines()
    
    linhas[idx] = novo_nome + '\n' 
    
    with open('habito.txt', 'w') as f:
        print("Aluno atualizado!")


def deletar():
    ler()
    idx = int(input("Digite o ID do habito que deseja excluir: "))
    
    with open('habito.txt', 'r') as f:
        linhas = f.readlines()
    
    del linhas[idx]
    
    with open('habito.txt', 'w') as f:
        f.writelines(linhas)
    print("habito removido!")


while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break



    elif opcao == '4': deletar()
    elif opcao == '5': break