jogador = {}
gols = []

jogador['NomeJogador '] = str(input("Nome do Jogador: "))
part = int(input("Quantas partidas ele jogou? "))

for i in range(0, part):
    gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print("-=" * 35)
print(jogador)
print("-=" * 35)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 35)

print(f"O jogador {jogador['NomeJogador']} jogou {part} partidas.")
for i in gols:
    print(f"  => Na partida {i+1}, fez {i} gols.")

