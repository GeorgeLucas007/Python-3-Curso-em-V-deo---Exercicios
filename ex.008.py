valor = float(input("Digite a distância em metros:"))

print("A medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm".format(valor, valor/1000, valor/100, valor/10, valor*10, valor*100, valor*1000))
