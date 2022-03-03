num = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatoze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    valor = int(input("Digite o valor desejado: [0 a 20] "))
    if 0 <= valor <= 20:
        print(f'Você digitou o número {num[valor]}.')
    else:
        print("Valor NÃO permitido.")

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if opcao == "N":
        break
