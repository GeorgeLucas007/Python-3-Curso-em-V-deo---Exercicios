somaidade = 0
maior = 0
menomulhe = 0
nomevelho = ""

for pessoa in range(1, 5):
    print("-----", pessoa,"º pessoa -----")

    nome = str(input("Nome:")).strip()
    idade = int(input("Idade:"))
    somaidade += idade
    genero = str(input("Gênero (F/M):")).strip()

    if genero == "m" or genero == "M":
        if idade > maior:
            maior = idade
            nomevelho = nome

    if genero == "f" or genero == "F":
        if idade < 20:
            menomulhe += 1

media = somaidade / 4
print("A media de idade do grupo é de {:.2f} anos".format(media))
print("O homem mais velho tem {} e se chama {}".format(maior, nomevelho))
print("Contabilizado {} mulheres com idade menor que 20".format(menomulhe))
