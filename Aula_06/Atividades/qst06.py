'''Lista de Convidados'''
convidados = ["Pelé", "Bruce Li", "Naruto", "Neymar", "Fernandinho"]

'''Convite '''
for nome in convidados:
    print(f"Bora pra balada, {nome}!")

'''Quem não poderar ir '''
print("Bruce Li: Não vou !")
print("Orochi: Não vou !")

'''Modifique sua lista, substitua os desistentes por novos convidados'''

convidados[1] = "Vini Jr"
convidados[2] = "Jair"

for nome in convidados:  
    print(f"Bora pra balada, {nome}!")