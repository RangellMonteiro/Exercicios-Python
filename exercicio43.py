#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
#- Acima de 40: Obesidade Mórbida
peso = float(input("Digite aqui seu peso: (KG)"))
altura = float(input("Digite aqui sua altura: "))
imc = peso / (altura **2)

if imc < 18.5:
    print("O imc dessa pessoa é {:.2f}".format(imc))
    print("Está abaixo do peso ideal")
elif imc >= 18.5 and imc < 25:
    print("O imc dessa pessoa é {:.2f}".format(imc))
    print("Está no peso ideal")
elif imc >= 25 and imc < 30:
    print("O imc dessa pessoa é {:.2f}".format(imc))
    print("Está com sobrepeso!")
elif imc >= 30 and imc < 40:
    print("O imc dessa pessoa é {:.2f}".format(imc))
    print("Está obesa!")
elif imc > 40:
    print("O imc dessa pessoa é {:.2f}".format(imc))
    print("Obesidade mórbida!!!")

