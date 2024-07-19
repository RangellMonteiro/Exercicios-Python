#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
atual= date.today().year
nascimento = int(input("Digite o ano de seu nascimento: "))
idade = atual - nascimento

if idade <= 19:
    print("Você tem {} anos e sua categoria é júnior".format(idade))
elif idade > 19 and idade <= 25:
    print("Você tem {} e sua categoria é sênior".format(idade))
elif idade > 25:
    print("Você tem {} anos e sua categoria é Master".format(idade))