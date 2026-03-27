compras = []
produtos = input("digite os seus produtos")

while produtos != "fim":
        compras = compras + [produtos]
        produtos = input("digite fim para finalizar a sua compra")
        
print("lISTA DOS PRODUTOS")
for item in compras:
        print(f"{item}")