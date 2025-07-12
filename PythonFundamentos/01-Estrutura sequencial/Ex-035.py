'''
Faça um programa que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado.
Autor:Jules do Nascimento Pires
Ex:035
'''
# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
ladoA = float(input("Lado A:"))
ladoB = float(input("Lado B:"))

# Cálculo
area = ladoA * ladoB

# Resultado
print("Área {}Cm".format(area))