import os

restaurantes = ["Domino's", "Kanzen"]

def exibir_nome_programa():
    print("""𝒮𝒶𝒷𝑜𝓇 𝐸𝓍𝓅𝓇𝑒𝓈𝓈
      """)
    
def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def fim_app():
    exibir_subtitulo("Finalizando o programa...")

def voltar_menu():
    input("\nDigite uma tecla qualquer para voltar ao menu principal. ")
    main()

def opcao_invalida():
    print("Opção inválida!\n")

def cadastrar_restaurante():
    exibir_subtitulo("A opção escolhida foi: Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu()


def listar_restaurante():
    exibir_subtitulo("Listando restaurantes...")
    for restaurante in restaurantes:
        print(f"{restaurante}")
    voltar_menu()



def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print("Ativar Restaurante")
        elif opcao_escolhida == 4:
            fim_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()