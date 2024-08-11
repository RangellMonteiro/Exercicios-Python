numeros = list()
menor = maior = 0
for cont in range(0,5):
    numeros.append(int(input("Digite um número para a posição {}: ".format(cont))))
    if numeros[cont] == max(numeros):
        maior = numeros[cont]
    elif numeros[cont] == min(numeros):
        menor = numeros[cont]
        
print("Você digitou os valores {}".format(numeros))
print("O maior valor digitado foi {} nas posiões ".format(maior), end='')

for i, n in enumerate(numeros):
    if n == maior:
        print("{}... ".format(i), end="")
print("\nO menor valor digitado foi {} nas posições ".format(menor), end='')
for i, n in enumerate(numeros):
    if n == menor:
        print("{}... ".format(i), end="")



    

