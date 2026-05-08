def converter(lista):
    nova_lista =  []
    for idade in lista:
        try:
            nova_lista.append(int(idade))
        except ValueError:
            print(f"'{idade}' não pôde ser convertido e por isso foi ignorado.")
    return nova_lista

def verificador(lista):
    for num in lista:
        if num != num // 1:
            return "Erro na conversão"
    return "Todos os números foram convertidos corretamente!"

idades = ["18", "25", "32", "18", "42"]

idades_convertidas = converter(idades)
print(verificador(idades_convertidas))