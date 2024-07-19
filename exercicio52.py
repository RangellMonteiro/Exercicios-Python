numero = int(input("Digite um número: "))
total = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print("\33[34m", end=' ')
        total += 1
    else:
        print("\33[m", end = ' ')
    print("{}".format(c), end= ' ')
print(" \n O número {} foi divisivel {} vezes".format(numero,total))

if total == 2:
    print("Ele é um número primo")
else:
    print("Ele não é número primo")
