#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['Nome'] = str(input("Nome: "))
aluno['Media'] = float(input("Média de {}: ".format(aluno['Nome'])))
if aluno['Media'] >= 7:
    aluno['Situação'] = "Aprovado"
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado!"


for k, v in aluno.items():
    print("{} : {}".format(k, v))


