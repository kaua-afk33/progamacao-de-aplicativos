dano = int(input("digite o seu dano"))
defesa = int(input("digite a defesa do vilao"))

dano = defesa - dano

if defesa <= dano:
    print("o seu dano foi afetivo" , dano)
elif defesa >= dano:
    print("vilao tomou critico")