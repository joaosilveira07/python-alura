def valor_total(valores):
    soma = 0
    for valor in valores:
        soma += int(valor)
    return soma

entrada = "111 296 600"
valores = entrada.split()
total = valor_total(valores)
print(f"O total das vendas foi de: {total}")