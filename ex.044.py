print('{:=^40}'.format("Evil Corp"))

preço = float(input("Preço total das compras R$"))

print("\n\nFORMAS DE PAGAMENTO")

print("[1] Á vista no dinheiro/cheque"
      "\n[2] Á vista no cartão"
      "\n[3] Em até 2x no cartão"
      "\n[4] 3x ou mais no cartão")

pagar = int(input("\nCOMO VAI PAGAR?:"))

if pagar == 1:
    print("Valor à pagar com 10% de desconto R${:.2f}".format(preço - (preço * 0.1)))

elif pagar == 2:
    print("Valor à pagar com 5% de desconto R${:.2f}".format(preço - (preço * 0.05)))

elif pagar == 3:
    print("Valor à pagar será normal R${:.2f} Dividido em 2x cada parcela será de R${:.2f}".format(preço, preço/2))

elif pagar == 4:
    parce = int(input("\nEm quantas parcelas voçê irá pagar?:"))

    if parce >= 3:
        valorJuros = preço + (preço * 0.2)
        print("Valor à pagar com 20% de juros R${:.2f}\n Será dividido em {}x, assim cada parcela fica no valor de R${:.2f}".format(valorJuros, parce, valorJuros/parce))

    else:print("PARCELAS INVÁLIDAS")

else: print("Forma de Pagamento DESCONHECIDO pelo sistema!!!")
