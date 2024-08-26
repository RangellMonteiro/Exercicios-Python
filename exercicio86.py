#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input("Digite um valor para [{}, {}]: ".format(l,c)))

for l in range(0, 3):
    for c in range(0, 3):
        print("[{:^5}]".format(matriz[l][c]), end=" ")
    print()
