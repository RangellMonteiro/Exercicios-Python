#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6), 'Jogador2': randint(1,6),'jogador3':randint(1, 6),
'Jogador4':randint(1,6)}
ranking = list()
print("Valores sorteados:")
for k, v in jogo.items():
    print("{} tirou {} no dado".format(k,v))
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("==Ranking dos jogadores==")
for i, v in enumerate (ranking):
    print("`{}º lugar: {} com {}".format(i + 1, v[0], v[1]))
    sleep(0.5)
