valores = []  #Um dos mais dificeis. Penei pra fazer. Dá pra resumir mais

for v in range(0, 5):
    valor = (int(input("Digite os valores: ")))

    if v == 0:
        valores.append(valor)

    if v == 1:
        if valor > valores[0]:
            valores.append(valor)

        if valor < valores[0]:
            valores.insert(0, valor)

    if v == 2:
        if valor > max(valores):
            valores.append(valor)

        if valor < min(valores):
            valores.insert(0, valor)

        if valores[0] > valor and valores[1] < valor:
            valores.insert(1, valor)

        if valores[0] < valor and valores[1] > valor:
            valores.insert(1, valor)

    if v == 3:
        if valor > max(valores):
            valores.append(valor)

        if valor < min(valores):
            valores.insert(0, valor)

        if valores[0] > valor and valores[1] < valor:
            valores.insert(1, valor)

        if valores[0] < valor and valores[1] > valor:
            valores.insert(1, valor)

        if valores[1] > valor and valores[2] < valor:
            valores.insert(2, valor)

        if valores[1] < valor and valores[2] > valor:
            valores.insert(2, valor)

    if v == 4:
        if valor > max(valores):
            valores.append(valor)

        if valor < min(valores):
            valores.insert(0, valor)

        if valores[0] > valor and valores[1] < valor:
            valores.insert(1, valor)

        if valores[0] < valor and valores[1] > valor:
            valores.insert(1, valor)

        if valores[1] > valor and valores[2] < valor:
            valores.insert(2, valor)

        if valores[1] < valor and valores[2] > valor:
            valores.insert(2, valor)

        if valores[2] > valor and valores[3] < valor:
            valores.insert(3, valor)

        if valores[2] < valor and valores[3] > valor:
            valores.insert(3, valor)

print(valores)
