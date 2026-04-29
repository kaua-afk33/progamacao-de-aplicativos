def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    # Aprovado se (Nota > 80 E XP > 2) OU se tiver certificação
    if (nota_teste > 80 and anos_xp > 2) or possui_certificacao:
        return True
    return False

nota = float(input("Nota do teste: "))
xp = int(input("Anos de experiência: "))
cert = input("Possui certificação? (S/N): ").upper() == 'S'

if verificar_aprovacao(nota, xp, cert):
    print("Resultado: Contratar")
else:
    print("Resultado: Descartar")