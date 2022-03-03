valores = []

while True:
    valor = (int(input("Digite os valores: ")))

    if valor in valores:
        print(f"Valor repetido. Não será adicionado.")
    else:
        valores.append(valor)
        print(f"valor adicionado")

    opcao = " "
    while opcao not in 'SN':
        opcao = str(input("Deseja Continuar?:")).upper().strip()[0]
    if opcao == 'N':
        break

valores.sort()
print(f"Os valores da lista são {valores}")







