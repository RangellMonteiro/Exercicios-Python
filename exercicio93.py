#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
partidas = list()
jogador['nome'] = str(input("Nome do jogador: "))
tot = int(input("Quantas partidas {} jogou? ".format(jogador["nome"])))
for c in range(0, tot):
    partidas.append(int(input("Quantos gols na partida {}? ".format(c))))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
    print("O campo {} tem o valor {}".format(k, v))
print("O jogador {} jogou {} partidas".format(jogador["nome"], len(jogador["gols"])))
for i, v in enumerate(jogador['gols']):
    print("=> Na partida {}, fez {} gols".format(i, v))
print("Foi um total de {} gols".format(jogador["total"]))
