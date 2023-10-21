#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
var = float(input("Digite um número: "))
print("O dobro de {} é {} e o triplo é {} \n e sua raiz quadrada é {:.1f}".format(var,var*2,var*3, var ** (1/2)))
