def filtrar(tamanho):
    nova_lista = []
    while len(nova_lista) < tamanho:
        num = int(input("Qual número você deseja colocar na lista? "))
        nova_lista.append(num)

    print(f"Números pares: ", end='')
    for i in nova_lista:
        if i % 2 == 0:
            print(i, end=' ')

tamanho_lista = int(input("Qual o tamanho você deseja que tenha a lista? "))
filtrar(tamanho_lista)