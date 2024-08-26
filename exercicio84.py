#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input("Nome:")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1]>maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    dados.clear()
    if continuar in "Nn":
        break

print("{} pessoas foram cadastradas".format(len(pessoas)))
print("O maior peso foi de {}kg. peso de ".format(maior), end=" ")
for p in pessoas:
    if p[1] == maior:
        print("[{}]".format(p[0]), end=" ")

print(" O menor peso foi de {}Kg".format(menor), end=" ")
for p in pessoas:
    if p[1] == menor:
        print("[{}]".format(p[0]), end=" ")
