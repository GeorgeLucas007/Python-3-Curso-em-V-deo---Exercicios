nome = (str(input("Digite seu nome:"))).strip()

print("Muito prazer em te conhecer!")

separa = nome.split()

print("Seu primeiro nome é {}".format(separa[0]))
print("Seu último nome é {}".format(separa[len(separa)-1]))


