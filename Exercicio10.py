#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
litros = area/2
print("Sua parede tem dimensão {} x {} e sua área é {}M². \n Para pintar essa parede, você precisará de {}L de tinta".format(largura,altura,area, litros))
