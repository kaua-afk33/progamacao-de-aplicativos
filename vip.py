ingresso = input("tem ingresso (S/N)")
idade = input("tem 18 ou mais (S/N)")
lista = input("esta na lista de convidado (S/N)")


if (idade >= 18 and ingresso == "S") or lista == "S":
   print("seja bem vindo")
else:
    print("acesso negado")


