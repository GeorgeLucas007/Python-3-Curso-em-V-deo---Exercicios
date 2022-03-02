reta_1 = float(input("Valor da primeira reta:"))
reta_2 = float(input("Valor da segunda reta:"))
reta_3 = float(input("Valor da terceira reta:"))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_3 + reta_1 and reta_3 < reta_1 + reta_2:
    if reta_1 == reta_2 == reta_3:
        print("TRIANGULO EQUILÁTERO")

    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print("TRIANGULO ISOSCELES")

    elif reta_1 != reta_2 != reta_3:
        print("TRIANGULO ESCALENO")

else: print("Não pode ser um triangulo!!!")
