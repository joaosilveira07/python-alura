pessoa = {
    "nome": "João",
    "idade": 18, 
    "cidade": "Campinas"
}

# pessoa['idade'] = 19 - Atribuição direta
pessoa.update({"idade":  19})
print(pessoa)

# pessoa["profissão"] = "Dev" - Forma de adicionar diretamente
pessoa.update({"profissão": "Dev", "Experiência": 1})
print(pessoa)

del pessoa["Experiência"] # Se a chave já não existir irá retornar KeyError
print(pessoa)
