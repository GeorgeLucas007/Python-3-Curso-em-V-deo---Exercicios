nome = str(input("Digite seu nome completo:")).strip() #<---- Elimina os espaços inuteis"

print("Seu nome maiusculo é {}".format(nome.upper()))
print("Seu nome minusculo é {}".format(nome.lower()))
print("Seu nome possui {} letras".format(len(nome) - nome.count(' '))) #<--- ler todos os caracteres e subtrai pela quantidade de espaços#

separa = nome.split() #separa cada palavra em uma lista

print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))  #<-- 0 corresponde ao primeiro nome

