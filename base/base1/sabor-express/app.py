import os

def exibir_nome_programa():
    print("""𝒮𝒶𝒷𝑜𝓇 𝐸𝓍𝓅𝓇𝑒𝓈𝓈
      """)
    
def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def fim_app():
    os.system('cls')
    print("Finalizando o programa...")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    print(f"Você escolheu a opção {opcao_escolhida}")

    if opcao_escolhida == 1:
        print("Cadastrar Restaurante")
    elif opcao_escolhida == 2:
        print("Listar Restaurante")
    elif opcao_escolhida == 3:
        print("Ativar Restaurante")
    else:
        fim_app()


def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()