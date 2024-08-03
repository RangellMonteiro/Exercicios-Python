# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
vitorias = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou impar? [P/I]")).strip().upper()[0]
    if tipo == "P":
        if total %2 == 0:
            print("Você venceu!")
            vitorias +=1
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if total %2 == 1:
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print("GAME OVER! Você venceu {} vezes".format(vitorias))                 



