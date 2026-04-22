numeros = [2, 6, 2, 3, 10, 5]
soma = 0
try:
    for num in numeros:
        soma += num
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
