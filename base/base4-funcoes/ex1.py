def calcula_idade():
    ano_nasc = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    idade = ano_atual - ano_nasc
    print(f"A idade é {idade} anos.")

calcula_idade()

def calcular(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

nascimento = int(input("Digite o seu ano de nascimento: "))
atual = int(input("Digite o ano atual: "))
idade = calcular(nascimento, atual)
print(f"A idade é {idade} anos.")