from time import sleep

def maior(*num):
    print("-="*30)
    print("Analisando os valores passados...")
    for i in num:
        print(i, end=" ")
        sleep(0.5)
    print(f"Foram informados {len(num)} ao todo.")
    print(f"O maior valor informado foi {max(num)}.")


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
