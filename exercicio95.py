#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input("Nome do jogador: "))
    tot = int(input("Quantas partidas {} jogou? ".format(jogador["nome"])))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input("Quantos gols na partida {}? ".format(c))))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper()[0]
        if continuar in "SN":
            break
        print("Erro! responda apenas S ou N")
    if continuar == "N":
        break
print("Cod", end=" ")
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print() 
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print("ERRO! não existe jogados com código {}".format(busca))
    else:
        print("-- LEVANTAMENTO DO JOGADOR {}:".format(time[busca]["nome"]))
        for i, g in enumerate(time[busca]['gols']):
            print("     No jogo {} fez {} gols.".format(i+1, g))
print("Volte sempre!")