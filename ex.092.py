from datetime import datetime
pessoa = {}

pessoa['nome'] = str(input("Nome: "))
nasceu = int(input("Ano de nascimento: "))
pessoa['idade'] = datetime.now().year - nasceu
pessoa['ctps'] = str(input("Carteira de Trabalho (0 não tem): "))

if pessoa['ctps'] == 0:
    print("-=" * 40)
    for k, v in pessoa.items():
        print(f" - {k} tem o valor {v}")
else:
    pessoa['contratação'] = int(input("Ano de contratação: "))
    pessoa['salário'] = float(input("Salário: R$"))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
    print("-=" * 40)
    for k, v in pessoa.items():
        print(f" - {k} tem o valor {v}")
