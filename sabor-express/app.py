import os
restaurantes = [
    {"nome":"Mr. Sam's", "categoria":"Hamburgueria", "ativo":True},
    {"nome":"Kanzen", "categoria":"Japonesa", "ativo":True},
    {"nome":"Espeto Tião", "categoria":"Salgados", "ativo":False}]

def exibir_nome_programa(): 
    """Essa função é responsável por sempre exibir o nome do programa na tela do usuário""" 
    print("""𝒮𝒶𝒷𝑜𝓇 𝐸𝓍𝓅𝓇𝑒𝓈𝓈 
    """) 

def exibir_opcoes():
    """Essa função é responsável por listar as possíveis opções que o usuário pode escolher""" 
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alternar estado do Restaurante")
    print("4. Sair\n")
     
def exibir_subtitulo(texto):
    """Essa função é responsável por exibir subtítulos""" 
    os.system('cls') 
    linha = "*" * (len(texto) + 4) 
    print(linha) 
    print(texto) 
    print(linha) 
    print() 

def fim_app():
    """função responsável por finalizar o programa""" 
    exibir_subtitulo("Finalizando o programa...") 

def voltar_menu():
    """ Essa função é responsável por dar ao usuário a opção de voltar ao menu principal nas escolhas 
    
    Outputs: - Volta o usuário para a função main
    """ 
    
    input("\nDigite uma tecla qualquer para voltar ao menu principal. ") 
    main() 
    
def opcao_invalida():
    """ Essa função é resposável por printar a mensagem de opção inválida caso o usuário digite uma opção inválida
     
    Outputs:
    -printa "Opção Inválida!" 
    """ 
    
    print("Opção inválida!\n") 
    
def cadastrar_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante 
    Inputs:
    - Nome do restaurante 
    - Categoria 
    
    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    """ 
    
    exibir_subtitulo("A opção escolhida foi: Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"nome": nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante) 
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu() 
    
def listar_restaurante():
    """função responsável por listar todos os restaurantes"""
    
    exibir_subtitulo("Listando restaurantes...") 

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado" 
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}") 
    voltar_menu() 
        
def alternar_estado_restaurante():
    """função responsável por alternar o estado do restaurante entre ativado/desativado""" 
    
    exibir_subtitulo("Alternando estado do restaurante...")
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ")
    restaurante_encontrado = False 
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True 
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante foi desativado com sucesso!" 
            print(mensagem) 
            if not restaurante_encontrado:
                print(f"O restaurante {nome_restaurante} não foi encontrado!") 
                
    voltar_menu() 
    
def escolher_opcao():
    """função responsável por fazer o usuário escolher uma opção válida e printar opção inválida caso ele escolha uma opção inválida"""
    
    try:
        opcao_escolhida = int(input("Escolha uma opção: ")) 
        print(f"Você escolheu a opção {opcao_escolhida}")
        if opcao_escolhida == 1:
            cadastrar_restaurante() 
        elif opcao_escolhida == 2:
            listar_restaurante() 
        elif opcao_escolhida == 3:
            alternar_estado_restaurante() 
        elif opcao_escolhida == 4:
            fim_app() 
        else:
            opcao_invalida() 
    except:
        opcao_invalida() 
        
def main():
    """função principal que inicia o programa"""
    os.system('cls') 
    exibir_nome_programa() 
    exibir_opcoes() 
    escolher_opcao() 
    
if __name__ == '__main__': 
    main()
