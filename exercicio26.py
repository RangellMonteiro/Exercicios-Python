#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

print("-==-"*20)
print("Irei pensar um número entre 0 e 5, tente advinhar!")
print("-==-"*20)
jogador = int(input("Em que número eu pensei: "))
computador = randint(0,5)
print("Processando...")
sleep(2)

if jogador == computador:
    print("Parabéns você conseguiu me vencer!")
else:
    print("Ganhei!, eu pensei no número {} e não no {}".format(computador, jogador))
