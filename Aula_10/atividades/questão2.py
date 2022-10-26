notas = []
acumuladora = 0
contador = 0

# Criação da lista das notas
for i in range(20):
    notas.append(float(input("Digite uma nota: ")))

# Soma
for nota in notas:
    acumuladora = acumuladora + nota


# Média
media = acumuladora / len(notas)

# Contador = contador + 1
for n in notas:
    if n > media:
        contador += 1

print(f"{contador} foram as notas acima da média.")