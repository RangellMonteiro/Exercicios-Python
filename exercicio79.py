numeros = list()
while True:
    n = (int(input("Digite um número: ")))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado!")
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    if continuar in "Nn":
        break
print("Você digitou os valores {}".format(sorted(numeros)))



