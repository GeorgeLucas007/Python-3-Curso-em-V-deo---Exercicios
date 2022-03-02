peso = float(input("Digite o peso(Kg):"))
altura = float(input("Digite a altura(m):"))

imc = (peso) / (altura**2)

if imc < 18.5:
    print("({:.2f}) Abaixo do peso".format(imc))

elif 18.5 <= imc < 25:
    print("({:.2f}) Peso ideal".format(imc))

elif 25 <= imc < 30:
    print("({:.2f}) Sobrepeso".format(imc))

elif 30 <= imc < 40:
    print("({:.2f}) Obesidade".format(imc))

else: print("({:.2f}) Obesidade Mórbida".format(imc))


