import random

alu_1 = str(input("Nome do primeiro aluno:"))
alu_2 = str(input("Nome do segundo aluno:"))
alu_3 = str(input("Nome do terceiro aluno:"))
alu_4 = str(input("Nome do quarto aluno:"))

lista = [alu_1, alu_2, alu_3, alu_4]

escolhi = random.choice(lista)

print("O aluno escolhido foi {}".format(escolhi))