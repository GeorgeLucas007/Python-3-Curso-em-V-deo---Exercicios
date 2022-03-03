primeValor = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
c = 1
total = 0
mais = 10

while mais!= 0:
    total += mais
    while c <= total:
        progre = primeValor + (c - 1) * razao
        print("{}".format(progre), end=" ")
        c += 1

    mais = int(input("\nQuantos termos você quer mostrar a mais? "))
print("progressão finalizada com {} termos mostrados.".format(total))

#Programa difícil