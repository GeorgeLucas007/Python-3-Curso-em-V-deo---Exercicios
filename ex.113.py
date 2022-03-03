num = ""
num2 = ""

while num != type(int):
    try:
        num = int(input("Digite um Inteiro: "))
        break

    except (ValueError, TypeError):
        print("ERRO: por favor, digite um número inteiro válido.")

while num2 != type(float):
    try:
        num2 = float(input("Digite um real: "))
        break

    except (ValueError, TypeError):
        print("ERR0: por favor, digite um número real válido.")