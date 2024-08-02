#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print("Gerador de PA v2.0")
print('-=' *10)
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiroTermo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print("{} -> ".format(termo), end=" ")
        termo += razao
        contador +=1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais?"))
print("Progressão finalizada com {} termos mostrados".format(total))