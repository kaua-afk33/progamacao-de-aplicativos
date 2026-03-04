saldo = 1000.00

print(" Bem-vindo ao banco Bancário ")
print("1  Depósito")
print("2  Saque")
print("3  Extrato")

opcao = input("Escolha uma opção")

if opcao == "1":
    valor_deposito = float(input("Digite o valor do depósito: R$ "))
    if valor_deposito > 0:
        saldo + valor_deposito
        print("Depósito de R$ valor_deposito: realizado com sucesso!")
    else:
        print("Operação cancelada: O valor deve ser maior que zero")

elif opcao == "2":
    valor_saque = float(input("Digite o valor do saque: R$ "))

    pode_sacar = valor_saque > 0 and (valor_saque <= saldo or valor_saque == 100.00)
    
    if pode_sacar:
        saldo = valor_saque
        print ("Saque de R$ valor_saque: autorizado")
    else:
        print("Saque não autorizado: Saldo insuficiente ou valor inválido")

elif opcao == "3":
    print("extrato")
    print("Saldo atual:" , saldo)

else:
    print("Opção inválida")
