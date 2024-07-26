#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for p in range(1,6):
    pesoPessoa = float(input("Peso da {}° pessoa: ".format(p)))
    if p == 1:
        maior = pesoPessoa
        menor = pesoPessoa
    else:
        if pesoPessoa > maior:
            maior = pesoPessoa
        if pesoPessoa < menor:
            menor = pesoPessoa    
print("O maior peso lido foi de {}KG".format(maior))
print("O menor peso lido foi  de {}KG ".format(menor))