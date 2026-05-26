def desconto(porcentagem):
    def preco_final(valor):
        valor_final = valor - (valor * (porcentagem / 100))
        return valor_final
    return preco_final

porcentagem_desconto = int(input("Digite a porcentagem de desconto: "))
valor_compra = int(input("Digite o valor da compra: "))

print(f"Preço final com desconto: {desconto(porcentagem_desconto)(valor_compra)}")