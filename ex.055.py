maior = 0

for pessoa in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(pessoa)))

    if peso > maior:
        maior = peso

print("Maior peso lido foi de {:.2f}Kg".format(maior))
