
autorizados = ["Alice", "Bob", "Carlos"]
print(f"Lista atual: {autorizados}")


nome = input("Digite o nome do pesquisador: ")


if nome in autorizados:
   
    indice = autorizados.index(nome)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")
    
  
    decisao = input(f"Deseja remover {nome} da lista? (Sim/Não): ")
    if decisao.lower() == "sim":
        autorizados.remove(nome)
        print(f"Pesquisador {nome} removido.")
        print(f"Lista atualizada: {autorizados}")
 else:
    print("Operação cancelada. A lista permanece a mesma.")

    cadastro = input(f"digite {nome} nao foi encontrado")
    if cadastro == "sim":
        autorizados.append(nome)
        print(f"pesquisador foi encontrado {autorizados}")



    

