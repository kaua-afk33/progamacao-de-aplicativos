def dobrar(numero):
    return numero * 2


assert dobrar(3) == 6
print("Teste 1 (dobrar(3) == 6): Passou!")

try:
    assert dobrar(0) == 1
    print("Teste 2: Passou!")
except AssertionError:
    print("Teste 2 (dobrar(0) == 1): Falhou como esperado!")

assert dobrar(-2) == -4
print("Teste 3 (dobrar(-2) == -4): Passou!")

print("\nFim dos testes!")