def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False

assert pode_entrar(25, False) is True, "Falhou: Maior de idade deve poder entrar"

assert pode_entrar(10, True) is True, "Falhou: Menor acompanhado deve poder entrar"

assert pode_entrar(15, False) is False, "Falhou: Menor desacompanhado não deve poder entrar"

assert pode_entrar(18, False) is True, "Falhou: 18 anos deve poder entrar"

assert pode_entrar(17, True) is True, "Falhou: 17 anos acompanhado deve poder entrar"

print("Todos os testes para 'pode_entrar' passaram com sucesso!")