x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x > 0 and y > 0:
    print(f"O valor de x é: {x} e o de y é: {y}, portanto o ponto se encontra no primeiro quadrante.")
elif x < 0 and y > 0:
    print(f"O valor de x é: {x} e o de y é: {y}, portanto o ponto se encontra no segundo quadrante.")
elif x < 0 and y < 0:
    print(f"O valor de x é: {x} e o de y é: {y}, portanto o ponto se encontra no terceiro quadrante.")
elif x > 0 and y < 0:
    print(f"O valor de x é: {x} e o de y é: {y}, portanto o ponto se encontra no quarto quadrante.")
else:
    print("O ponto está localizado no eixo ou origem.")