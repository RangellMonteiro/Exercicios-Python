#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaColuna = 0

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input("Digite um valor para [{}, {}]: ".format(l,c)))

for l in range(0, 3):
    for c in range(0, 3):
        print("[{:^5}]".format(matriz[l][c]), end=" ")
        if matriz[l][c] % 2 ==0:
            somaPar += matriz[l][c]
    print()
print("A soma dos valores pares é {}".format(somaPar))
for l in range(0,3):
    somaColuna += matriz[l][2]
print("A soma dos valores da terceira coluna é {}".format(somaColuna))
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print("O maior valor da segunda linha é {}".format(maior))
