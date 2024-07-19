#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = float((input("Primeiro segmento: ")))
reta2 = float((input("Segundo segmento:")))
reta3 = float(input("Terceito segmento:"))

if reta1 < reta2 + 3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos podem formar um triângulo")
else:
    print("Os segmentos não podem formar um triângulo")

