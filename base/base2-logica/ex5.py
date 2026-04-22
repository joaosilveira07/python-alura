despesas = float(input("Digite o total de despesas no mês (R$): "))
print(f"O total de despesas é de: {despesas}")

if despesas > 3000:
    print("Você ultrapassou o limite do orçamento, gaste com cuidado!")
else:
    print("Você está dentro do orçamento.")