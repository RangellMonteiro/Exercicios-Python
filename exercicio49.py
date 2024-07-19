#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Digite um número para ver sua tabuada: "))
contador = 0
for c in range(1, 11):
    contador = contador + 1
    print("{} x {:2} = {}".format(numero, contador, numero*contador))