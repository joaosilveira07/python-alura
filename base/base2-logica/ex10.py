renda = float(input("Digite qual a sua renda mensal: "))
valor_parcela_desejada = float(input("Digite qual o valor da parcela desejada: "))

if renda <= 2000:
    print("Empréstimo negado: Renda insuficiente")
elif valor_parcela_desejada > (renda * 0.3):
    print("Empréstimo negado: parcela acima de 30% da renda.")
else:
    print("Empréstimo aceito com sucesso!")