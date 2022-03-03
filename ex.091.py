from random import randint

jogadores = dict()
listaJogadores = list()


for i in range(0, 3):
    jogadores['Nome: '] = str(input(f"Digite o nome do {i+1}ª jogador: "))
    jogar = str(input('Para jogar o dado aperte [J]: ')).strip().upper()[0]
    if jogar == "J":
        jogadores['Resultado: '] = randint(1, 6)
        print("Seu resultado foi registrado. Aguarde para os outros jogadores.")
    else:
        jogadores['Resultado: '] = -1
        print("Já que você não apertou [J] seu resultado será -1 e está desclassificado")
    listaJogadores.append(jogadores.copy())

for i in listaJogadores:
    print(i['Nome: '], end="-->")
    print(i['Resultado: '])





