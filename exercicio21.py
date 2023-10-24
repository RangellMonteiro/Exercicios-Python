#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from time import sleep
num = int(input("Digite aqui um número: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("Analisando o número {}...".format(num))
sleep(1)
print("Unidade {}".format(unidade))
print("Dezena {}".format(dezena))
print("Centena {}".format(centena))
print("Milhar {}".format(milhar))