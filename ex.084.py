dados = list()
pessoas = list()
quant = 0

while True:
    dados.append(str(input('Nome:')))
    dados.append(str(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S ou N] ")).upper().strip()[0]
    if opcao == "N":
        print("Programa encerrado...")
        break

for p in pessoas:
    if p[1] >= max(p[1]):
        print(f'O mais pesado é {p[0]} e pesa {p[1]}')

    else:
        print(f'O menos pesado é {p[0]} e pesa {p[1]}')