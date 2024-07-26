#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
contadorMaiores = 0
contadorMenores = 0
for c in range(1,8):
    nascimento= int(input("Em que ano a {}° pessoa nasceu? ".format(c)))
    idade = atual - nascimento
    if idade >= 21:
        contadorMaiores += 1
    else:
        contadorMenores += 1 
print("Ao todo tivemos {} pessoas maiores de idade".format(contadorMaiores))
print("E também tivemos {} pessoas menores de idade".format(contadorMenores))
        