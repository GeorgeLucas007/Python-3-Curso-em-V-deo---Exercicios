#Fiz sem ser com o assunto dessa aula. Não precisei das listas.Na verdade n fiz, o meu deu um erro.
palavra = str(input("Digite a expressão: "))

for indice in palavra:
    if indice == ')' and indice == '(':
        print("Expressão inválida.")
    else:
        break


if palavra.count('(') == palavra.count(')'):
    print("Expressão válida.")
else:
    print("Expressão inválida.")



#comparar os indices com contadores. se os contadores forem iguais para cada pedaço do pareteses a expressao é aceita (se fizer com listas).







#Resolução dos comentarios do video
"""expr = str(input("Digite uma expressão:"))
pilha = 0
for cont in expr:
    if cont == "(":
        pilha += 1
    if cont == ")":
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0:
    print("Sua expressão é valida!!!")
else:
    print("Sua expressão é invalida!!!")"""