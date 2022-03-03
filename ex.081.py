lista = []

while True:
    lista.append(int(input("Digite um valor: ")))

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar?[S ou N] ")).upper().strip()[0]
    if opcao == 'N':
        break

print(f"\nA lista tem {len(lista)} elementos.")

lista.sort(reverse=True)
print(f"\nLista em ordem descrecente {lista}.")

if 5 in lista:
    print("\nValor 5 foi encontrado na lista.")
else:
    print("\nValor 5 não encontrado na lista.")