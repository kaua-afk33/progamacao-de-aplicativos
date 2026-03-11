user_id = int(input("digite o seu id"))
valor_compra = float(input("digite o valor da compra"))

if user_id % 2 == 0 and valor_compra > 500.00:
    print(f"Parabéns, usuário {user_id}! Você ganhou um cupom para sua compra de R$ {valor_compra}.")
else:
    print(f"Obrigado pela compra, usuário {user_id}. Continue acompanhando nossas promoções!")