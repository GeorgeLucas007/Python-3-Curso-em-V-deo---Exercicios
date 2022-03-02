from datetime import date

atual = date.today().year
maior_idade = atual - 18

cont = 0
cont1 = 0

for pess in range(1, 8):
    nasceu = int(input("Em que ano a {}ª pessoa nasceu? ".format(pess)))

    if nasceu > maior_idade:
        cont += 1

    if nasceu < maior_idade:
        cont1 += 1


print("Ao todo tivemos {} pessoas maiores de idade".format(cont1))
print("E também tivemos {} pessoas menores de idade".format(cont))
