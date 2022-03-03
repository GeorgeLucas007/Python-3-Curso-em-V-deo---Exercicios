def terreno(x, y):
    print(f"A área de um terreno {larg}x{comp} é de {larg*comp}m².")

print("Controle de Terrenos")
print("-"*20)
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))

terreno(larg, comp)
