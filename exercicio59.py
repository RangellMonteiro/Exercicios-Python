#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
from time import sleep
opcao = 0
numero1 = int(input("Primeiro valor: "))
numero2 = int(input("Segundo valor: "))
while opcao != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do Programa ''')
    opcao = int(input("Qual sua opção? "))
    if opcao == 1:
        soma = numero1 + numero2
        print("A soma entre {} e {} é {}". format(numero1,numero2, soma))
    elif opcao == 2:
        multiplicacao = numero1 * numero2    
        print("A multiplicação entre {} e {} é {}". format(numero1,numero2, multiplicacao))
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print("Entre {} e {} o maior é {}".format(numero1,numero2,maior))        
    elif opcao == 4:
        print("Informe os números novamente: ") 
        numero1 = int(input("Primeiro valor: "))
        numero2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Saindo do programa...")
    sleep(1)
print("Fim do programa")
