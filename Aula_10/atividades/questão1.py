clubes = []

for i in range(10):
    clube = input("Digite o novo clube: ")
    clubes.append(clube)

clube_pesquisar = input("Procure um clube: ")


for c in clubes:
    if clube_pesquisar.upper() == str(c).upper():
        print("Achei!")
    else:
        print("Não achei")