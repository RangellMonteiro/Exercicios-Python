# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
valor = float(input("Digite um valor: "))
print("O valor digitado foi {} e sua porção inteira é {}".format(valor, math.trunc(valor)))