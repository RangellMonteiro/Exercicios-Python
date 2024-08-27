#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
lista = list()
jogos = list()
jogadas = int((input("Quantos jogos deseja mostrar? ")))
total = 1
while total <= jogadas:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print("Sorteando {} jogos".format(jogadas))

for i, l in enumerate(jogos):
    print("Jogo {}: {}".format(i,l))



