#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input("Dias alugados:  "))
km = float(input("KM rodados: "))
valorQuilometragem = 0.15 * km
aluguel = 60 * dias
total = valorQuilometragem + aluguel
print("O total a pagar é R${}, R${} pelo alugel e R${} pela quilometragem".format(total,aluguel,valorQuilometragem))