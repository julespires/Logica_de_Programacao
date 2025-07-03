'''
Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
a) O número digitado ao quadrado;
b) O número digitado ao cubo;
c) A raiz quadrada do número;
d) a raiz cúbica do número digitado;
Autor:Jules do Nascimento Pires
Ex:011
Versão:V1
Data:03/07/2025
'''
# Bibliotecas usadas
import os
import math

# Limpa a tela
os.system('cls')

# Entrada de dados
num = int(input("Digite um número:"))

# Resultado
print("O número {} ² = {}".format(num,(num ** 2)))
print("O número {} ³ = {}".format(num,(num ** 3)))
print("A raiz quadrada de {} = {}".format(num,(math.sqrt(num))))
print("A raiz cúbica de {}  = {}".format(num,(math.pow (num, 1/3))))