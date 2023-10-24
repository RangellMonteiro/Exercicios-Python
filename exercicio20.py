#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input("Digite seu nome: ")).strip()
print("O nome digitado com todas as letras maiúsculas {}".format(nome.upper()))
print("O nome digitado com todas as letras minúsculas {}".format(nome.lower()))
print("O nome digitado tem ao todo {}".format(len(nome) - nome.count(" ")))