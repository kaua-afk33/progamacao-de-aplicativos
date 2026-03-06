garrafas = int(input("quantas garrafas foi produzidas"))

alerta_disparo = False 

if garrafas % 100 == 0:
    print("amostra de teste")
    alerta_disparo = True

if garrafas %500 == 0:
    print("para a maquina imediatemente")
    alerta_disparo = True
    

if not alerta_disparo:
    print(f"producao em dia. garrafas numero [{garrafas}] processo.")