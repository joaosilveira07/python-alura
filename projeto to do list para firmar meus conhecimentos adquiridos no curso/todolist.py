import os

def titulo():
    print("""
Ｔｏ－Ｄｏ Ｌｉｓｔ
""")
    
def opcoes():
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Alternar estado da tarefa (Completa/Incompleta)")
    print("4. Remover Tarefa")

def voltar_menu():
    input("Digite qualquer tecla para voltar ao menu. ")
    main()



def main():
    titulo()
    opcoes()

if __name__ == '__main__': 
    main()