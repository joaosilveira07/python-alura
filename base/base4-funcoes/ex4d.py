def convertor(lista):
    nova_lista = []
    ignorados = []
    for valor in lista:
        try:
            nova_lista.append(int(valor))
        except ValueError:
            ignorados.append(valor)
    return nova_lista, ignorados


dados = ["11987654321", "abc", "21912345678", "xyz", "31987654321"]
dados_convertidos, ignorados = convertor(dados)
print(dados_convertidos)
print(f"Esta lista teve {len(ignorados)} erros.")
print(f"Valores ignorados: {ignorados}")