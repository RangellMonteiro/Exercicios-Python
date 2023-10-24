#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input("Digite um ângulo: "))
seno = math.sin(math.radians(angulo))
print("O ângulo de {}° tem o seno de {}°".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print("O ângulo de {}° tem o cosseno de {}°".format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {}° tem o tangente de {}°".format(angulo,tangente))

