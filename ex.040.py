nota_1 = float(input("Digite sua primeira nota:"))
nota_2 = float(input("Digite sua segunda nota:"))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print("Tirando {:.2} e {:.2}, a média do aluno é {}\n O aluno está APROVADO.".format(nota_1, nota_2, media))

elif media >= 5 and media < 7:#Poderia ser if 7 > media >= 5. O PYTHON aceita
    print("Tirando {:.2} e {:.2}, a média do aluno é {}\n O aluno está em Recuperação.".format(nota_1, nota_2, media))

else:print("Tirando {:.2} e {:.2}, a média do aluno é {}\n O aluno está REPROVADO.".format(nota_1, nota_2, media))
