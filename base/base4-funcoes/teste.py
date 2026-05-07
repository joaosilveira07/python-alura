def ola_mundo(nome):
    return print(f"Olá, {nome}")
ola_mundo("João")

def somar(a, b):
    soma = a + b
    return soma

def cumprimentar(nome = "Visitante"):
    print(f"Olá, {nome}!")

cumprimentar()
cumprimentar("João")

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
print(fatorial(5))

def multiplicador(n):
    def multiplica(x):
        return x * n
    return multiplica
triplo = multiplicador(3)
valor = triplo(5)
print(valor)

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar
bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(bom_dia("Vini"))
print(boa_noite("Ana"))