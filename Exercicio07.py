#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input("Digite uma distância em metros: "))
print("{}CM\n{}MM".format(metros/1000,metros*1000))