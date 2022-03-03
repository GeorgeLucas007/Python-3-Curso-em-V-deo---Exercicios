n = int(input("Quantos termos da sequência de Fibonacci  você quer? "))
d = n - 2
c = 0
numA = 1
numB = 0
print("0 -> 1", end = "")

while c < d:
    num = numA + numB
    numB = numA
    numA = num
    c += 1
    print(" -> {}".format(num), end = "")
