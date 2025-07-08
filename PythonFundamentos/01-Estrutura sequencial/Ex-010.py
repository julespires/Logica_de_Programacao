'''
Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = p * R2.
Autor:Jules do Nascimento Pires
Ex:010
Versão:V1
Data:03/07/2025
'''

# Bibliotecas
import math
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
raio = float(input("Valor do raio:"))

# Cálculo
area = math.pi * raio ** 2

# Resultado
print("Área do círculo {}:cm".format(area))

# Fim