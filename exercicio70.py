#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = totmil = menor = cont = 0
barato = ""
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preco: R$ "))
    cont += 1
    total += preco
    if preco > 1000:
        totmil +=  1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ""
    while resp not in "Sn":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("Fim do programa!")
print("O total da compra foi R${:.2f}".format(total))
print("Temos {} produtos custando mais de R$1000.00")
print("O produto mais barato foi {} que custa R${:.2f}".format(barato,menor))         