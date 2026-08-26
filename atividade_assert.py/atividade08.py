def pode_votar(idade):
 	return idade >= 16


assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True

print("teste1: não pode votar")
print("teste2: pode votar")
print("teste3: pode votar")