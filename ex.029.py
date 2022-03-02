velocidade = float(input("Qual é a velocidade atual do carro em Km/h?-->"))

multa = (velocidade - 80) * 7

if velocidade <= 80:
    print("Bom dia. Siga seu caminho em segurança.")

if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h.\nVocê deve paga uma multa de R${:.2f}!".format(multa))