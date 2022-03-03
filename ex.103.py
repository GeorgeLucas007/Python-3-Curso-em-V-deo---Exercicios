def ficha(nome= "Desconhecido", g=0):
    print(f"O jogador {nome} fez {g} gol(s) no campeonato.")



#Programa Principal
nome = str(input("Nome do jogador: "))
gols = str(input("Numero de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(g=gols)
else:
    ficha(nome, gols)