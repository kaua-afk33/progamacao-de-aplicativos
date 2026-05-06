estoque = []
acao = 0
def adicionar_produto(nome):
    nome = input("Digite o nome do produto: ")
    estoque.append(nome)

def listar_produtos(estoque):
    for item in estoque:
        print(f"{estoque.index(item)} - {item}")

def atualizar_produto(indice, produto):
    indice = int(input("Qual o indice do produto ?: "))
    produto = input("Qual o nome do produto ?: ")
    estoque[indice] = produto

def remover_produto(indice):
    indice = int(input("Qual o indice do produto a ser removido ?: "))
    removido = estoque[indice]
    estoque.pop(indice)
    print(f"Item {removido} removido. ")

def exibir_menu(acao):
    while acao != 5:
        print("\n1 - Adicionar produto")
        print("\n2 - Listar produtos ")
        print("\n3 - Atualizar produto ")
        print("\n4 - Remover produto ")
        print("\n5 - Fechar menu")
        acao = int(input("Qual ação deseja realizar ?: "))

        if acao == 1:
            adicionar_produto(acao)
        elif acao == 2:
            listar_produtos(estoque)
        elif acao == 3:
            atualizar_produto(acao, acao)
        elif acao == 4:
            remover_produto(acao)
        elif acao == 5:
            return
        
exibir_menu(acao)
print("Menu fechado. ")