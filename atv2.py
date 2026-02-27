nota = float(input("digite a sua nota"))
presenca = int(input("digite a sua presenca"))

if nota >= 7.0 and presenca >= 75:
    print("voce passou de ano")
elif nota >= 7.0 and presenca < 75:
    print("voce reprovou por falta")
elif nota <= 7.0 and presenca >= 75:
    print("voce reprovou por nota")