from random import randint
c = 0
print("=-" * 30)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 30)

while True:
    valor = int(input("Diga um valor: "))
    opcao = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    if opcao != "P" and opcao != "I": # Tem que ajeitar pq se digitar um Í o codigo para.
        print("Você digitou uma letra incorreta. Programa finalizado!")
        break

    print("-" * 30)
    PC = randint(0, 10)
    soma = PC + valor
    print(f"Você jogou {valor} e o computador {PC}.", end="")

    if soma % 2 == 0 and opcao == "P":
        print(f"Total deu {soma} Deu PAR")
        print("--" * 30)
        print("Você VENCEU!\nVamos jogar novamente...")

    if soma % 2 == 0 and opcao == "I":
        print(f"Total deu {soma} Deu PAR")
        print("--" * 30)
        print("Você PERDEU!")
        break

    if soma % 2 == 1 and opcao == "I":
        print(f"Total deu {soma} Deu ÍMPAR")
        print("--" * 30)
        print("Você VENCEU!\nVamos jogar novamente...")

    if soma % 2 == 1 and opcao == "P":
        print(f"Total deu {soma} Deu ÍMPAR")
        print("--" * 30)
        print("Você PERDEU!")
        break

    c += 1

print(f"GAME OVER! Você venceu {c} vezes.")
