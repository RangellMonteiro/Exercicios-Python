# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro = int(input("Primeiro valor:"))
segundo = int(input("Segundo valor: "))
terceiro = int(input("Terceiro valor: "))

#Verifica quem é menor
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

#Verifica quem é o maior
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))


