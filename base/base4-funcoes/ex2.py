def contar_caractere(palavra):
    return len(palavra)

texto = input("Digite uma palavra: ")
print(f"Essa palavra tem {contar_caractere(texto)} caracteres.")
