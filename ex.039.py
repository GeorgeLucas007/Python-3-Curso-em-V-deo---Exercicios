from datetime import date
atual = date.today().year

ano_nasceu = int(input("Digite o ano do seu nascimento:"))

idade = atual - ano_nasceu
anosAlis = (idade - 18)

if idade < 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(ano_nasceu, idade, atual))
    print("Ainda faltam {} anos para o alistamento.".format(abs(anosAlis)))  ## abs() deixar um valor em MODULO
    print("Seu alistamento será em {}.".format(idade + ano_nasceu + abs(anosAlis)))

elif idade > 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(ano_nasceu, idade, atual))
    print("Voçê já deveria ter se alistado há {} anos.".format(anosAlis))
    print("Seu alistamento foi em {}.".format(idade + ano_nasceu - anosAlis))

else: print("Quem nasceu em {} tem {} anos em {}.\nVoçê tem que se alistar IMEDIATAMENTE!".format(ano_nasceu, idade, atual))




