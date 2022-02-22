carKm = float(input("Quantidade de kilometros percorridos?"))
diaAluga = int(input("Quantos dias alugados?"))

pagaDia = diaAluga * 60
pagaKm = carKm * 0.15

total = pagaDia + pagaKm

print("O total a pagar é de R${:.2f}".format(total))