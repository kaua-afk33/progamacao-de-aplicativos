nota = float(input("sua nota no colegio passado"))
renda = float(input("seu redimento familiar"))
escola_publica = input("veio de escola publica (S/N)")

if (nota >= 8.0 and renda < 2.000) or escola_publica == "S":
    print("voce ganhou a bolsa")

else:
    print("Nao passou")
