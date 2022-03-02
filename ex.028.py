from random import randint
from time import sleep

computador = randint(0,5) # O computador vai sortear um número de 0 a 5.

print('---' * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('---' * 20)
jogador = int(input("Em que número pensei?-->")) #Valor que o jogador vai digitar entre 0 e 5.
print("PROCESSANDO...")
sleep(2)

if jogador == computador:
    print("Parabéns!!! Você acertoooou.")

else:
    print("Você errou. Pensei no número {} e não no {}. Tente Novamente... ".format(computador, jogador))

