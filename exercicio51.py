#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimoTermo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo,decimoTermo + razao, razao):
    print(c, end= "->")
print("Acabou!")

