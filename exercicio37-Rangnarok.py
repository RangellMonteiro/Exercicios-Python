#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Qual número deseja converter?"))
print('''Digite a base de conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
base = int(input("Sua opção: "))

if base == 1:
    print("O número {} convertido para binário fica {}".format(num, bin(num)[2:]))
elif base == 2:
    print("O número {} convertido para octal fica {}".format(num, oct(num)[2:]))
elif base == 3:
    print("O número {} convertido para hexadecimal fica {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida")

