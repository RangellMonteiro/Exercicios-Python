# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input("Qual a velocidade atual do carro?: "))
if velocidade <= 80:
    print("Tenha um bom dia e dirija com segurança!")
elif velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Multado! você excedeu o limite que é de 80KM/H Você deve pagar uma multa de {:.2f}R$".format(multa))
    print("Tenha um bom dia e dirija com segurança!")