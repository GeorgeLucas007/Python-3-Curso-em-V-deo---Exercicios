aluno = {}
alunoss = []

for i in range(0,2):
    aluno['nome: '] = str(input("Nome do aluno: "))
    aluno['média: '] = float(input("Média do aluno: "))
    alunoss.append(aluno.copy()) #Não posso esquecer desse metodo copy()

print(alunoss)