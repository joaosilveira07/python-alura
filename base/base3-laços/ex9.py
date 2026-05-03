livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    else:
        print(f"Livro disponível: {livro["nome"]}")

pessoa = {"nome": "João", "idade": 18}
pessoa["idade"] = 19
print(pessoa["idade"])
pessoa["profissão"] = "Desenvolvedor"
print(pessoa)
pessoa["peso"] = 92
print(pessoa)
del pessoa["peso"]
print(pessoa)