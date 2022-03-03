valores = list()

for v in range(0, 5):
    valores.append(int(input(f'Digite o {v}ª valor da lista: ')))

print(f"Você digitou os valores {valores}")

print(f"O maior valor digitado foi {max(valores)} nas posições ", end="")
for indice, valor_indice in enumerate(valores):
    if valor_indice == max(valores):
        print(f"{indice}...", end="")

print(f"\nO menor valor digitado foi {min(valores)} nas posições ", end="")
for indice_2, valor_indice_2 in enumerate(valores):
    if valor_indice_2 == min(valores):
        print(f"{indice_2}...", end="")





