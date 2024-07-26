#Jogo da advinhação v2
from random import randint
from time import sleep

print("-==-"*20)
print("Irei pensar um número entre 0 e 10, tente advinhar!")
print("-==-"*20)
computador = randint(0,10)
acertou = False
contadorPalpites = 0
while not acertou:
    jogador = int(input("Qual palpite?: "))
    print("Processando...")
    sleep(1)
    contadorPalpites += 1
    if jogador == computador:
        acertou = True
        print("Parabéns você conseguiu me vencer!")
    else:
        if jogador < computador:
            print("Mais...tente novamente")
        else: 
            print("Menos...tente novamente")
print("Acertou com {} palpites".format(contadorPalpites))
