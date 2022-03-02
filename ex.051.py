primeiValor = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão entre os valores: "))

for num in range(1, 11):
    an = primeiValor + (num - 1) * razao
    print(an, end=" ")
