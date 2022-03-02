from time import sleep
from random import choice

print("""Suas Opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA""")

jogada = int(input("Qual é a sua jogada? "))

if jogada == 0:
    jogada = str("PEDRA")

elif jogada == 1:
    jogada = str("PAPEL")

elif jogada == 2:
    jogada = str("TESOURA")

else:print("OPÇÂO INVÁLIDA!!!")

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

lista = ["PEDRA", "PAPEL", "TESOURA"]
jogaPC = choice(lista)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Computador jogou {}".format(jogaPC))
print("Jogador jogou {}".format(jogada))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

if jogada == "PEDRA" and jogaPC == "PEDRA":
    print("JOGADORES EMPATARAM")

elif jogada == "PEDRA" and jogaPC == "PAPEL":
    print("COMPUTADOR VENCEU")

elif jogada == "PEDRA" and jogaPC == "TESOURA":
    print("JOGADOR VENCEU")


if jogada == "PAPEL" and jogaPC == "PEDRA":
    print("JOGADOR VENCEU")

elif jogada == "PAPEL" and jogaPC == "PAPEL":
    print("JOGADORES EMPATARAM")

elif jogada == "PAPEL" and jogaPC == "TESOURA":
    print("COMPUTADOR VENCEU")


if jogada == "TESOURA" and jogaPC == "PEDRA":
    print("COMPUTADOR VENCEU")

elif jogada == "TESOURA" and jogaPC == "PAPEL":
    print("JOGADOR VENCEU")

elif jogada == "TESOURA" and jogaPC == "TESOURA":
    print("JOGADORES EMPATARAM")
