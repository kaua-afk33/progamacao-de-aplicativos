lista = ["Ocupado", "Livre", "Ocupado", "Livre"]

vaga = int(input("digite de 0 a 3"))

if 0 <= vaga <= 3:
    if vaga % 2 == 0 and lista[vaga] == "ocupado":
        print(f"vaga {vaga} autorizada")
    else:
        print(f"vagas {vaga} indisponivel")
else:
    print("vagas invalidas")
    
