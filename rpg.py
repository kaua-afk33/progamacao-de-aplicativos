vida = 5664

def sofrer_dano(valor_dano):
    nova_vida = nova_vida - valor_dano
    return nova_vida
print("O jogo começou vida" ,vida)

while vida > 0:
    dano_causado = int(input("Quanto de dano o monstro causou"))
    vida = sofrer_dano(vida, dano_causado)
    if vida > 0:
        print(f"Você sofreu {dano_causado} de dano. Vida restante: {vida}")
    else:
        print("Você sofreu dano Vida restante: 0")
print("game over")
