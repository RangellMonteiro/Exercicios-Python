# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        impares.append(v)
print("A lista completa é {}".format(numeros))
print("A lista de pares é {}".format(pares))
print("A lista de ímpares {}".format(impares))