valores = [2, 4, 5, 10, 12, 22]
soma = 0
for numero in valores:
    soma += numero

print(f"A soma de todos os números é de: {soma}")

try:
    media = soma / len(valores)
    print(f"A média dos valores é: {media:.2f}")
except ZeroDivisionError as e:
    print(f"A lista está vazia, não foi possível calcular a média: {e}")
