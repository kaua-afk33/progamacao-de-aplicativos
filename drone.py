codigo = int(input("Digite o Código do Drone: "))
autorizacao = input("Possui autorização da torre? (s/n):")


if codigo == 999 or autorizacao == "s":
    print("identificação confirmada iniciando análise de voo")

    bateria = int(input("Nível da Bateria 0 a 100"))
    clima = input("Clima ensolarado/chuvoso")
    vento = float(input("Velocidade do Vento km/h"))

    
    if bateria < 10:
        print("ALERTA: Bateria fraca")
        print("POUSO AUTORIZADO: Iniciando descida")
    
    
    else:
        sol_seguro = (clima == "ensolarado" and vento < 30.0)
        chuva_segura = (clima == "chuvoso" and vento < 10.0)

        if sol_seguro or chuva_segura:
            print("POUSO AUTORIZADO:Iniciando descida")
        else:
            print("POUSO NEGADO:Condições meteorológicas perigosas")
else:
    print("ERRO 01: Drone não identificado retornando a base")