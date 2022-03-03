primeiValor = int(input("Digite o primeiro valor da progressão: "))
razao = int(input("Digite a razão da PA: "))
c = 1

while c < 11:
    progre = primeiValor + (c - 1) * razao
    print("{}".format(progre), end=" ")
    c += 1