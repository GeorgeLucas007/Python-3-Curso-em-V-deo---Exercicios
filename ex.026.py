frase = str(input("Digite uma frase:")).strip().lower()

print("A letra A aparece {} vezes na frase.".format(frase.count("a")))
print("A primeira letra a apareceu na posição {}".format(frase.find("a")))
print("A última letra a apareceu na posição {}".format(frase.rfind("a")))