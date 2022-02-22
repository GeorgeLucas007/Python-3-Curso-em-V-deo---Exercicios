from math import hypot

Co = float(input("Comprimento do cateto oposto:"))
Ca = float(input("Comprimento do cateto adjacente:"))

hipo = hypot(Co, Ca)

print("A hipotenusa vai medir {:.2f}".format(hipo))