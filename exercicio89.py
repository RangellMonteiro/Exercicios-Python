#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input("Quer continuar? [S/N]")).strip().upper()
    if continuar in "Nn":
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opcao = int(input("Mostrar notas de qual aluno? (999 intemrrompe):"))
    if opcao == 99:
        break
    if opcao <= len(ficha) - 1:
        print("Notas de {} são {}".format(ficha[opcao][0], ficha[opcao][1]))

