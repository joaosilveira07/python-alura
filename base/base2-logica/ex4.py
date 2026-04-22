peso = float(input("Digite seu peso em kg's: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc < 25:
    print("Seu peso está normal!")
else:
    print("Você está acima do peso!")