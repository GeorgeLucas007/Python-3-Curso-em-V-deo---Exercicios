from datetime import date #biblioteca que importa a data atual do PC.

ano = int(input("Que ano você quer analisar? Coloque 0 para analisa o ano atual-->"))

if ano == 0:
    ano = date.today().year #importa o ano atual do PC.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO".format(ano))