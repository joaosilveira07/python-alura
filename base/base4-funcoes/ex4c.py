def convertor(lista):
    nova_lista = []
    for preco in lista:
        try:
            nova_lista.append(float(preco))
        except ValueError:
            print(f"'{preco}' não pôde ser convertido e por isso foi ignorado.")
    return nova_lista

def verificador(lista):
    for num in lista:
        if type(num) != float:
            return "Erro na conversão"
    return "Todos os números foram convertidos corretamente!"

precos = ["19.90", "5.50", "102.00", "8.75"]
precos_convertidos = convertor(precos)
print(precos_convertidos)
print(verificador(precos_convertidos))