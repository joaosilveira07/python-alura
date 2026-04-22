distancia = float(input("Digite a distância percorrida (em km): "))

if distancia <= 100:
    pedagio = 10
elif distancia <= 200:
    pedagio = 20
else:
    pedagio = 30

print(f"Valor do pedágio é de R${pedagio}.")