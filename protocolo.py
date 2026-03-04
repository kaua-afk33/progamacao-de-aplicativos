cargo = input("qual e o seu cargo")
codigo = input("digite a senha")
botao_de_emergencia = input("acionar o botao de emergencia (S/N)")
equipamento = input("tem equipamento de protecao (S/N)")

if (cargo == "engenheiro" or cargo == "tecnico") and (codigo == "1234" or botao_de_emergencia == "S") and equipamento == "S": 
     print("acesso liberado")

else:
    print("acesso negado")
             