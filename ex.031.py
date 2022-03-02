viajem = float(input("Quantos Km tem sua viajem?-->"))

if viajem <= 200:
    valor1 = viajem * 0.50
    print("Como sua viajem tem {}Km o valor da passagem fica R${:.2f}".format(viajem, valor1))
else:
    valor2 = viajem * 0.45
    print("Como sua viajem tem {}Km o valor da passagem fica R${:.2f}".format(viajem, valor2))

''' poderia fazer assim: valor = viajem * 0.50 if viajem <= 200 else viajem * 0.45'''
