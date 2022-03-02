num_1 = float(input("Digite o primeiro valor:"))
num_2 = float(input("Digite o segundo valor:"))

if num_1 > num_2:
    print("O {:.2} é maior que o {:.2}".format(num_1, num_2))

elif num_1 < num_2:
    print("O {:.2} é maior que o {:.2}".format(num_2, num_1))

else: print("O {:.2} é igual ao {:.2}".format(num_1, num_2))
