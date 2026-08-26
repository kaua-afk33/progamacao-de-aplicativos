def buscar_nome(lista, nome):
    return nome in lista

print("--- Testes de buscar_nome ---")

resultado_vazia = buscar_nome([], "Ana")
print(f"Lista vazia buscando 'Ana': {resultado_vazia}")
assert resultado_vazia is False

resultado_um = buscar_nome(["Carlos"], "Carlos")
print(f"Lista com 1 elemento buscando 'Carlos': {resultado_um}")
assert resultado_um is True

resultado_ausente = buscar_nome(["Ana", "Bruno", "Carla"], "Daniel")
print(f"Lista com vários elementos buscando 'Daniel': {resultado_ausente}")
assert resultado_ausente is False


def tem_senha_valida(senha):
    return len(senha) >= 8

print("\n--- Testes de tem_senha_valida ---")

resultado_vazia = tem_senha_valida("")
print(f"Senha vazia: {resultado_vazia}")
assert resultado_vazia is False

resultado_pequena = tem_senha_valida("1234567")
print(f"Senha com 7 caracteres: {resultado_pequena}")
assert resultado_pequena is False

resultado_limite = tem_senha_valida("12345678")
print(f"Senha com 8 caracteres: {resultado_limite}")
assert resultado_limite is True