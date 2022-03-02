from random import randint
pal = 0
tenta = 1
print("Sou seu computador...\n"
      "Acabei de pensar em um número entre 0 e 10.\n"
      "Será que você consegue adivinhar qual foi?")

computador = randint(0, 10)
pal = int(input("Qual é seu palpite? "))

while pal != computador:
    if pal > computador:
        print("Menos... Tente mais uma vez.")
    if pal < computador:
        print("Mais... Tente mais uma vez.")

    pal = int(input("Qual é seu palpite? "))
    tenta += 1

print("Você acertou com {} tentativas".format(tenta))
