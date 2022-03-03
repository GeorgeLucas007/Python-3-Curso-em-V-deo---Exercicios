def leiaInt(x):
    while True:
        if x.isnumeric():
            return x
        while x != type(int):
            print("\033[0;31mErro! Digite um número inteiro válido.\033[m")
            x = leiaInt(input("Digite um número: "))
            break




#Programa Principal
n = leiaInt(input("Digite um número: "))
print(f"Você acabou de digitar o numero {n}")