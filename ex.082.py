valores = []
par = []
impar = []

while True:
    valores.append(int(input("Digite um valor: ")))

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar?[N ou S] ")).upper().strip()[0]
    if opcao == "N":
        break

print(f"{valores}")

for indice, valor_indice in enumerate(valores):
    if valor_indice % 2 == 0:
        par.append(valor_indice)
    else:
        impar.append(valor_indice)

print(f"{par}")
print(f"{impar}")



