'''
 Faça um programa que receba dois números, calcule e mostre a subtração do primeiro número pelo segundo.
 Autor:Jules do Nascimento Pires
 Ex-026
'''
# Biblioteca
import os

os.system('cls')

# Entrada dos dados
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

# Cálculo da subtração com variável
sub = num1 - num2

# Resultado
print("A subtração entre {} - {} = {}".format(num1, num2, sub))