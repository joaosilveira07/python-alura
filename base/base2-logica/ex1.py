venda_maca = int(input("Quantas maçãs foram vendidas neste mês? "))
venda_banana = int(input("Quantas bananas foram vendidas neste mês? "))

if venda_maca > venda_banana:
    print("As maçãs tiveram mais vendas!")
elif venda_maca == venda_banana:
    print("As maçãs e bananas venderam igualmente neste mês.")
else:
    print("As bananas tiveram mais vendas!")