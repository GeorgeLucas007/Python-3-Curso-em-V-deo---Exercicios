c = mascu = femi = 0

while True:
    idade = int(input("Qual a sua idade? "))
    if idade > 18:
        c += 1

    sexo = str(input("Qual seu sexo? [M/F] ")).upper().strip()[0]
    if sexo == "M":
        mascu += 1
    if idade < 20 and sexo == "F":
        femi += 1
    if sexo != "M" and sexo != "F":
        print("Programa encerrado!")
        break

    opcao = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if opcao == "N":
        print("Programa encerrado!")
        break

    print("==" * 30)

print("==" * 30)
print(f"{c} pessoas tem mais de 18 anos.")
print(f"{mascu} homens foram cadastrados.")
print(f"{femi} mulheres tem menos de 20 anos de idade.")

#            Resolução do Guanabara
"""
tot18 = totH = totM20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totH += 1
    if sexo == "F" and idade < 20:
        totM20 += 1
    res = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break
print(f"Total de pessoa coma mais de 18 anos: {tot18}")
print(f"Ao todo temos {totH} homens cadastrados")
print(f"E temos {totM20} mulheres com menos de 20 anos')
"""