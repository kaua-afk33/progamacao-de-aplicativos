def criar():
    destino = input("Para onde deseja viajar: ")
    with open('viagens.txt', 'a') as f:
        f.write(destino + '\n')
    print("Local cadastrado!")


def ler():
    with open('viagens.txt', 'r') as f:
        viagens = f.readlines()
        
        i = 0
        for viagem in viagens:
            print(f"{i} - {viagem.strip()}") 
            i += 1  

def atualizar():
    ler() 
    idx = int(input("Digite o ID do local que você deseja alterar: "))
    novo_local = input("Novo local: ")
    
    with open('viagens.txt', 'r') as f:
        linhas = f.readlines()
    
    linhas[idx] = novo_local + '\n' 
    
    with open('viagens.txt', 'w') as f: 
        f.writelines(linhas)
    print("Local atualizado!")


def deletar():
    ler()
    idx = int(input("Digite o ID do destino que deseja excluir: "))
    
    with open('viagens.txt', 'r') as f:
        linhas = f.readlines()
    
    del linhas[idx]
    with open('viagens.txt', 'w') as f:
        f.writelines(linhas)
    print("Local removido!")


while True:
    print("\n 1 cadastrar / 2 listar / 3 editar / 4 excluir / 5 sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break