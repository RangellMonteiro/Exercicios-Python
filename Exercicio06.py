#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota: "))
media = float((nota + nota2)/2)
print("A média entre {:.2f} e {} é igual a {:.2f}".format(nota,nota2,media))