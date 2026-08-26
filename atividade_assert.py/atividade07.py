#def classificar_idade(idade):
    #if idade < 12:
        #return "Criança"
    #elif idade < 18:
        #return "Adolescente"
    #elif idade > 18:          #no > tinha que ser >= 18 pois se a idade for 18 ou maior sera considerado adulto
        #return "Adulto"
    #else:
        #return "Menor de idade"


def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade >= 18:
        return "Adulto"
    else:
        return "Idade inválida"


print(f"Teste 1 (10 anos): {classificar_idade(10)}") 
print(f"Teste 2 (18 anos): {classificar_idade(18)}")  
print(f"Teste 3 (25 anos): {classificar_idade(25)}") 