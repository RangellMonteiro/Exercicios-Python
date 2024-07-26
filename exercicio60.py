#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input("Digite um número para calcular seu fatorial: "))
contador = numero
fatorial = 1
print("Calculando {}! = ".format(numero), end='')
while contador > 0:
    print("{}". format(contador), end='')
    print(" X " if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador-= 1
print("{}".format(fatorial))