def juntar(produto, preco):
    produto = produto.split(",")
    preco = preco.split(",")
    for i in range(len(produto)):
        print(f"{produto[i].strip()}: {preco[i].strip()}")
        

itens = input("Digite os produtos separados por vírgula: ")
valores = input("Digite os preços separados por vírgula: ")
juntar(itens, valores)