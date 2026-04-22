a = int(input("Informe os dias necessários para a atividade A: "))
b = int(input("Informe os dias necessários para a atividade B: "))
c = int(input("Informe os dias necessários para a atividade C: "))

"""
if (a >= 0 and b >= 0 and c >= 0):
    total = a + b + c
    print(f"O tempo total para completar esse projeto é de {total} dias.")
else:
    print("Erro: Os dias não podem ser negativos.")
"""

if (a < 0 or b < 0 or c < 0):
    print("Erro: Os dias não podem ser negativos.")
else:
    print(f"O tempo total para completar este projeto é de {a + b + c} dias.")