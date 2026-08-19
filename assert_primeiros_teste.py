def eh_par(numero):
    return numero % 2 == 0

assert eh_par(4) is True, "Falhou: 4 deveria ser considerado par"

assert eh_par(7) is False, "Falhou: 7 deveria ser considerado ímpar"

assert eh_par(0) is True, "Falhou: 0 deveria ser considerado par"

assert eh_par(-2) is True, "Falhou: -2 (par negativo) deveria ser considerado par"
assert eh_par(-3) is False, "Falhou: -3 (ímpar negativo) deveria ser considerado ímpar"

print("Todos os testes passaram com sucesso!")