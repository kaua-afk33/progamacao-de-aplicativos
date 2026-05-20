import json

with open("notas.json", "r", encoding="utf-8") as arquivo:
    notas = json.load(arquivo)

soma = notas["matemática"] + notas["portugues"]

print("Soma das notas:", soma)