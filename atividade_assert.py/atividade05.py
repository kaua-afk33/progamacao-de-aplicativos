def frete_gratis(valor):
    return valor >= 200

def pode_votar(idade):
    return idade >= 16

def senha_valida(senha):
    return len(senha) >= 8

assert frete_gratis(199.99) is False "Abaixo do limite sem frete grátis"
assert frete_gratis(200.0) is True   "Exatamente no limite com frete grátis"
assert frete_gratis(200.01) is True  "Acima do limite com frete grátis"


assert pode_votar(15) is False "Abaixo do limite não pode votar"
assert pode_votar(16) is True  "Exatamente no limite pode votar"
assert pode_votar(17) is True  "Acima do limite pode vota"


assert senha_valida("1234567") is False  "Abaixo do limite 7 caracteres"
assert senha_valida("12345678") is True  "exatamente no limite 8 caracteres"
assert senha_valida("123456789") is True "Acima do limite 9 caracteres"


print("Todos os testes de limite passaram com sucesso!")

