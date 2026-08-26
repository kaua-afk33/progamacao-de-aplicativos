def situacao_faltas(faltas):
 	0 a 4: "Regular"
 	 5 a 10: "Atenção"
 	 11 ou mais: "Reprovado por falta"
 	pass

def situacao_faltas(faltas):
    if faltas <= 4:
        return "Regular"
    elif faltas <= 10:
        return "Atenção"
    else:
        return "Reprovado por falta"
