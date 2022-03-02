somatorio = 0
cont = 0

for num in range(3, 501, 3):
    if num % 2 == 1:
        somatorio += num       #ACUMULADOR
        cont += 1              #CONTADOR
print("A soma de todos os {} valores solicitados é {}".format(cont, somatorio))



