soma = c = 0

while True:
    valor = int(input("Digite um valor [999 para parar]: "))
    if valor == 999:
        break
    c += 1
    soma += valor

print(f"A soma dos {c} valores foi {soma}!")#Nova forma de printar no Python 3.6+