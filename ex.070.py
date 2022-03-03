print('--' * 30)
print("{: ^60}".format("Lojas GL"))
print("--" * 30)
soma = p = c = menor = 0
barato = " "

while True:
    produto = str(input("Nome do Produto: ")).strip()

    preco = float(input("Preço: R$"))
    c += 1
    if c == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        p += 1
    soma += preco

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao == "N":
        break

print("{:-^40}".format("Fim do Programa"))
print(f"O total da compra foi R${soma:.2f}")
print(f"Temos {p} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor}")