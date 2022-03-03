num = 0
soma = 0
c = -1

while num != 999:
    num = int(input("Qual o valor desejado? [999 para parar]: "))
    soma += num
    c += 1

print("{} foram digitados e a soma entre eles foi {}".format(c, soma - 999))

#Código não foi feito da melhor maneira