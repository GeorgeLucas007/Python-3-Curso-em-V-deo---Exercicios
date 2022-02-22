valor = float(input("Quanto dinheiro você tem na carteira? R$"))

dolar = valor / 4.24

print("Com R${} você pode comprar US${:.2f}".format(valor, dolar))