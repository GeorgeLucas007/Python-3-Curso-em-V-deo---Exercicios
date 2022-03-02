valor = int(input("Você quer o fatorial de: "))
c = valor
f = 1

print("Calculando {}!=".format(valor), end=' ')

while c > 0:
    print("{}".format(c), end=" ")
    print("x " if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

