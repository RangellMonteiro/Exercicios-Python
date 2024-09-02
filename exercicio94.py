#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F] ")).upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print("Erro! por favor digite M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper()[0]
        if continuar in "SN":
            break
        print("ERRO! Responda apenas S ou N")
    if continuar == "N":
        break
print("Ao todo temos {} pessoas cadastradas".format(len(galera)))
media = soma / len(galera)
print("A média de idade é de {:5.2f} anos.".format(media))
print("As mulheres cadastradas foram ", end="")
for p in galera:
    if p['sexo'] in "Ff":
        print("{}".format(p["nome"]), end=" ")
print()
print("Lista das pessoas que estão com a idade acima da média: ", end=' ')
for p in galera:
    if p['idade']>= media:
        print("     ")
        for k, v in p.items():
            print("{} = {};".format(k,v), end=' ')
        print()
print("<<Encerrado>>")


