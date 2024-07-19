#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
acumulador = 0
contador = 0
for c in range(1,7):
    numero = int(input("Digite o {} valor: ".format(c)))
    if numero % 2 == 0:
        acumulador += numero
        contador += 1
print("Você digitou {} números pares e a soma foi {}".format(contador, acumulador))
 