from datetime import date

atual = date.today().year
nascimento = int(input("Informe o ano de nascimento do atleta:"))
idade = atual - nascimento

if idade <= 9:
    print("MIRIM")

elif 9 < idade <= 14:
    print("INFANTIL")

elif 14 < idade <= 19:
    print("JUNIOR")

elif 19 < idade <= 25:
    print("SÊNIOR")

else:print("MASTER")