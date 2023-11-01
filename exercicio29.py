#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Qual é a distância da sua viagem? "))
print("Você esta prestes a realizar uma viagem de {:.2f}KM".format(distancia))
if distancia <=200:
    valor = distancia * 0.50
    print("E o preço da sua passagem será R${:.2f}".format(valor))
elif distancia > 200:
    valor = distancia * 0.45
    print("E o preço da sua passagem será R${:.2f}".format(valor))

