#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro:"))
numero3 = int(input("Digite mais um número inteiro:"))
maior = numero
if numero > numero2 and numero > numero3:
    maior = numero

if numero2 > numero and numero2 > numero3:
    maior = numero2

if numero3 > numero and numero3 > numero2:
    maior = numero3
print("O maior número digitado foi {}".format(maior))
