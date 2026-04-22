hora_atual = int(input("Digite qual o horário atual (formato 24 horas): "))
print(f"Agora são {hora_atual} horas.")

"""
if hora_atual >= 8 and hora_atual <= 18:
    print("Acesso liberado com sucesso!")
else:
    print("Acesso negado!")
"""

if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")