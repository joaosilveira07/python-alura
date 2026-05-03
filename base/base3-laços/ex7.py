estoque = int(input("Digite qual a capacidade total de seu estoque: "))

while estoque >= 0:
    print(f"Venda Realizada! Estoque restante: {estoque}")
    estoque -= 1

print("Estoque Esgotado!")