#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))
print("Com {} você pode comprar {:.2f}$".format(dinheiro, dinheiro/5.05)) #Valor segundo a cotação do dia 15/10/2023