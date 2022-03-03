nums = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")),
        int(input("Digite um número: ")))

print(f"Você digitou os valores {nums}")
print(f"O valor 9 apareceu {nums.count(9)} vezes.")
print(f"O primeiro valor três está na posição {nums.index(3)+1}")
print("Os valores pares digitados foram ", end="")
for n in nums:
    if n % 2 == 0:
        print(n, end="")
