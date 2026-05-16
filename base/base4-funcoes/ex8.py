subtracao = lambda a, b: a - b
soma = lambda a, b: a + b
divisao = lambda a, b: a / b if b != 0 else "Erro: Divisão por zero"
multiplicacao = lambda a, b: a * b

print("=====CALCULADORA=====")
print("1. Soma")
print("2. Subtração")
print("3. Divisão")
print("4. Multiplicação")
opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print(f"O resultado é: {soma(a, b)}")
elif opcao == 2:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print(f"O resultado é: {subtracao(a, b)}")
elif opcao == 3:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print(f"O resultado é: {divisao(a, b)}")
else:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print(f"O resultado é: {multiplicacao(a, b)}")