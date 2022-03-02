valor = int(input("Digite o valor para ver sua tabuada(Multiplicação): "))

for num in range(1, 11):
    multi = valor * num
    print("{} x {} = {}".format(valor, num, multi))
