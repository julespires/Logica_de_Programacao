'''
Faça um programa que receba dois valores digitados pelo usuário e imprima o maior entre eles.
Autor:Jules do Nascimento Pires
Ex:001
'''

import os

# Limpa a tela
os.system('cls')

# Entrada de dados
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

# Condições
if num1 > num2:
    print("O numero {} é o maior!".format(num1))
if num2 > num1:
    print("O número {} é o maior! ".format(num2))

# Fim