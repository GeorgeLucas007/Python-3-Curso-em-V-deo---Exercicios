salario = float(input("Digite o seu salário:"))

if salario > 1250:
    aumento1 = salario + (salario * 0.1)
    print("Como seu salário era R${} com o aumento ficou R${} ".format(salario, aumento1))

if salario <= 1250:
    aumento2 = salario + (salario * 0.15)
    print("Como seu salário era R${} com o aumento ficou R${}".format(salario, aumento2))

