#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
numeros = list()
cont = 0
while True:
    numeros.append(int(input("Digite um valor: ")))
    cont += 1
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    if continuar in "Nn":
        break
print("Você digitou {} elementos.".format(cont))
numeros.sort(reverse=True)
print("Os valores em ordem decrescente são {}".format(numeros))
if 5 in numeros:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")

        



