idade = int(input("Digite sua idade: "))

if idade <= 12:
    print(f"\nVocê é uma criança!")
elif idade <= 18:
    print(f"\nVocê é um adolescente!")
elif idade > 18:
    print(f"\nVocê é um adulto!")
else:
    print(f"\nIdade inválida.")