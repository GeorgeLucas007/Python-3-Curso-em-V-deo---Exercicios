largura = float(input("Largura da Parede em metros:"))
altura = float(input("Altura da Parede em metros:"))

area = largura * altura
litros = (1*area) / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(largura, altura, area))
print("Para pintar essa parede, você precisará de {}l de tinta".format(litros))