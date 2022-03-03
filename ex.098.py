from time import sleep

def contador(x, y, z):

    print("-=" * 30)
    if z < 0:
        z = z * (-1)

    if x > y:
        for i in range(x, y+(-z), -z):
            print(i, end=" ")
            sleep(0.5)
        print("FIM!")
    else:
        for i in range(x, y+z, z):
            print(i, end=" ")
            sleep(0.5)
        print("FIM!")


# Programa principal

contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
