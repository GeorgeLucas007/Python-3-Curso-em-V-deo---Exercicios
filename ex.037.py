num = int(input("Digite um número inteiro:"))

print("Escolha uma das bases para conversão:\n"
      "[ 1 ] converter para BINÁRIO\n"
      "[ 2 ] converter para OCTAL\n"
      "[ 3 ] converter para HEXADECIMAL")

opção = int(input("Sua opção: "))

if opção == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num).replace("0b", "")))

elif opção == 2:
    print("{} convertido para OCTAL é igual a {}" .format(num, oct(num).replace("0o", "")))

elif opção == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num).replace("0x", "")))

else: print("Valor inválido. FAÇA NOVAMENTE!")



