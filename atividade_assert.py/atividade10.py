def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif 15 <= temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"


assert classificar_temperatura(10) == "Frio"

assert classificar_temperatura(15) == "Agradável"

assert classificar_temperatura(20) == "Agradável"

assert classificar_temperatura(25) == "Agradável"

assert classificar_temperatura(30) == "Quente"

print("Todos os 5 testes passaram com sucesso!")