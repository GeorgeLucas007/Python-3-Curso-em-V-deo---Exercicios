from datetime import datetime


def voto(x):
    resu = ""
    idade = datetime.now().year - x

    if idade < 16:
        resu = str(f"Com {idade} anos: NÃO VOTA.")

    elif 16 <= idade < 18 or idade >= 70:
        resu = str(f"Com {idade} anos: VOTO OPCIONAL.")

    elif 18 <= idade < 70:
        resu = str(f"Com {idade} anos: VOTO OBRIGATÓRIO.")

    return resu


# Programa Principal
print("-="*30)
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
