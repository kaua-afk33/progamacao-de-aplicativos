curso = input("voce concluiu o curso de segurança? (S/N)")

if curso == "S":
    print("pode passar")
instrutor = input("o instrutor esta na sala (S/N)")
print("pode passar")
if curso == instrutor == "S":
    print("pode passar")
else:
    ("acesso negado conclua o curso")
