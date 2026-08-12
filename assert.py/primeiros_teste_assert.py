def definir_idade(idade):
    # Avalia antes de prosseguir
    assert idade >= 0, "A idade não pode ser negativa!"
    return f"Idade definida: {idade}"

# Execução normal (passa silenciosamente)
definir_idade(25)

# Interrupção com erro
definir_idade(-5)
# Resultado: AssertionError: A idade não pode ser negativa!