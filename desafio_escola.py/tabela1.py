def cadastrar_escola():
    print("\n" + "=" 40)
    print("COMEÇANDO O CADASTRO DA ESCOLA")
    print("\n" "=" 40)
    nome = input("nome da escola: ")
    quandidade_de_alunos = int(input("quandidade de alunos na escola: "))
    id_escola = input("digite o ID da escola: ")

    try:
  
        assert len(nome) > 0, "O nome da escola não pode estar vazio."
        
        assert len(codigo) >= 3, "O código da escola deve ter pelo menos 3 caracteres."
        
        assert alunos_str.isdigit(), "A quantidade de alunos deve conter apenas números inteiros."
        quantidade_alunos = int(alunos_str)
        assert quantidade_alunos >= 0, "A quantidade de alunos não pode ser negativa."

        escola = {
            "codigo": codigo,
            "nome": nome,
            "alunos": quantidade_alunos
        }
        escolas.append(escola)
        print("Escola cadastrada com sucesso!")
        
    except AssertionError as e:
        print(f"\n[Erro de Validação]: {e}")
        print("Cadastro cancelado devido a dados inválidos.")


def listar_escola():
    try:
        def listar_escolas():
    print("\n" + "="*30)
    print("      LISTA DE ESCOLAS")
    print("="*30)

    assert isinstance(escolas, list), "O banco de dados de escolas deve ser uma lista."
    
    if not escolas:
        print("Nenhuma escola cadastrada no momento.")
        print("="*30)
        return
        
    for i, e in enumerate(escolas, 1):

        assert isinstance(e, dict), f"O registro {i} está corrompido."
        assert "codigo" in e and "nome" in e and "alunos" in e, f"O registro {i} possui campos faltando."
        
        print(f"[{i}] Código: {e['codigo']}")
        print(f"    Nome:   {e['nome']}")
        print(f"    Alunos: {e['alunos']}")
        print("-" * 30)


def atualizar_escola():
    print("\n" + "=" 40)
    print("ATUALIZAR ESCOLA: ")
    print("\n" "=" 40)

    try:
        assert len(escolas) > 0 "nao tem escolas para atualizar"

        id_busca = input("digite o ID da escola que voce queira atualizar: ")
        assert len(id_busca) > 0 "o codigo de busca nao pode estar vazio: "

        escola_encontrada = None 
        for e in escolas:
            if e {'id'} == id_busca:
                escola_encontrada = e
                break
        
        assert escola_encontrada is not None, "Escolas com codigo  {'id_busca'} nao foi encontrada. "

        print(f"Escola encontrada {escola_encontrada['nome']} insira os novos dados: ")

        nome_novo = input("digite a nova escola: ")
        novo_aluno = int(input("digite a nova quantidade de alunos: "))

        assert len(nome_novo) > 0, "o novo nome da escola nao pode estar vazio: "
        assert novo_aluno(), "a quantidade de alunos deve ser so numeros interios: "
        assert nova_quantidade_alunos >= 0, "a quantidade de alunos não pode ser negativa: "

        escola_encontrada ['nome'] = novo_nome
        escola_encontrada ['alunos'] = nova_quantodade_alunos
        print("Escolas atualizada com sucesso: ")
        print("Atualização cancelada: ")
        