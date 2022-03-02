from time import sleep

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
    print(" \n [ 1 ] Somar\n [ 2 ] Multiplicar\n [ 3 ] Maior\n [ 4 ] Novos Números\n [ 5 ] Sair do programa")
    opcao = int(input(">>>>>>>>> Qual é sua escolha? "))

    if opcao == 1:
        soma = valor1 + valor2
        print("A soma é: {}".format(soma))

    elif opcao == 2:
        multi = valor1 * valor2
        print("A multiplicação é: {}".format(multi))

    elif opcao == 3:
        if valor1 > valor2:
            print("{} é maior que {}".format(valor1, valor2))
        elif valor2 > valor1:
            print("{} é maior que {}".format(valor2, valor1))
        else: print("Valores iguais")

    elif opcao == 4:
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))

    elif opcao == 5:
        print("Finalizando programa...")
        sleep(2)

    else: print("Valor fora das opções!")

print("Programa Finalizado. Até mais.")

