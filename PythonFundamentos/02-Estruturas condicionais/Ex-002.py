'''
Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão
tirar para serem aprovados, considerando que a média exigida é 6,0.
Autor:Jules do Nascimento Pires
Ex:002
'''

#Biblioteca
import os

os.system('cls')

# Entrada de dados
nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terçeira nota:"))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3


# Condições
if (media >= 0.0 ) and (media <= 3.0):

    print(" Média = {media} Aluno reprovado!")

if(media > 3.0) and (media <= 7.0):

    print(" Média = {media} Fazer exame!")

if (media > 7.0) and (media <= 10.0):

    print("Média = {media} Aluno aprovado!")

# Fim