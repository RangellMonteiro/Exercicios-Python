from datetime import date
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("Que ano quer analisar? coloque 0 para analisar o ano atual "))
if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bisexto".format(ano))
else:
    print("O ano {} não é bisexto".format(ano))
