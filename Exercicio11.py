#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input("Digite o valor do produto: R$"))
desconto = (5 * preço) / 100
valorFinal = preço - desconto
print("O produto que custava R${}, na promoção com desconto de 5% vai custar {:.2f}R$".format(preço,valorFinal))