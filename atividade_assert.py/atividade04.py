def eh_par(numero):
    return numero % 2 == 0

"Correção: O número 3 não é par, logo o teste deve esperar False,"
"ou devemos testar com um número par (como o 4)"
assert eh_par(3) is False
"ou"
"assert eh_par(4) is True"

print("testes passaram com sucesso")