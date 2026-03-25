lista = livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []

emprestado = input("digite o livro que voce deseja")

if emprestado in livros_disponiveis:
    livros_disponiveis.remove(emprestado)
    livros_emprestados.remove(emprestado)
else:
    print("descupa esse livro nao esta disponivel")

emprestado = input("qual livro voce esta devolvendo")
if emprestado in livros_emprestados:
    livros_emprestados.remove(emprestado)
    livros_disponiveis.append(emprestado)
else:
    print("este livro nao e emprestado")

del livros_disponiveis[0:2]
print(f"final das duas lista {livros_disponiveis} {livros_emprestados}")
