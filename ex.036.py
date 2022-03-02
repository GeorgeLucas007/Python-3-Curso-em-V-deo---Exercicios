valor_casa = float(input("Qual o valor referente a casa? -->R$"))
salario_comprador = float(input("Qual é o salário do comprador?-->R$"))
anos_pagar = int(input("Em quantos anos você pretende pagar?--> "))

presta_mensal = (valor_casa) / (anos_pagar * 12)

print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valor_casa, anos_pagar, presta_mensal))


if presta_mensal > (salario_comprador * 0.3):
    print("EMPRÉSTIMO NEGADO!")

else: print("Empréstimo CONCEDIDO!")


