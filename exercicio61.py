#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print("Gerador de PA v2.0")
print('-=' *10)
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiroTermo
contador = 1

while contador <= 10:
    print("{} -> ".format(termo), end=" ")
    termo += razao
    contador +=1
print("FIM!")




