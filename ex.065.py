opçao = ""
valor = c = soma = media = 0

while opçao != "N":#Escolha falha pq o usuário pode apertar qualquer tecla diferente de 'N' que vai continuar
    valor = int(input("Digite um valor: "))
    opçao = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    soma += valor
    c += 1

    if c == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

media = soma / c
print("Você digitou {} números e a média entre eles foi {}".format(c, media))
print("O maior valor foi {} e o menor foi {}.".format(maior, menor))
