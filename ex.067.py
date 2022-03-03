while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print("-" * 25)
    for c in range(1, 11):
        mult = valor * c
        print(f"{valor} x {c} = {mult}")
    print("-" * 25)
print("Programa finalizado com sucesso.")
