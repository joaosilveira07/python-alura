x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x == 0 or y == 0:
    print("O ponto está localizado no eixo de origem.")
else:
    match (x > 0, y > 0):
        case(True, True):
            print("Primeiro quadrante.")
        case(False, True):
            print("Segundo quadrante.")
        case(False, False):
            print("Terceiro quadrante.")
        case(True, False):
            print("Quarto quadrante.")