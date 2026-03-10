
id_funcional = int(input("Digite o seu ID "))
temperatura = float(input("Digite a temperatura da máquina "))
tempo_uso = float(input("Digite o tempo de uso horas"))

if (id_funcional % 3 == 0) and (temperatura > 40 or tempo_uso > 8):
    print(f"Funcionário {id_funcional}, você foi escalado para a manutenção preventiva hoje")
else:
    print(f"Funcionário {id_funcional}, sua máquina opera dentro dos padrões normais")