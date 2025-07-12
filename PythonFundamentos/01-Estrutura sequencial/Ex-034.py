'''
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: 
A = ((base maior + base menor) * altura)/2
Autor:Jules do Nascimento Pires
Data:11/07/2025
Ex:034
'''
# Biblioteca
import os

# Limpa tela
os.system('CLS')

# Entrada de dados
baseMaior = float(input("Base maior:"))
baseMenor = float(input("Base menor:"))
altura = float(input("Altura:"))

# Cálculo
area = ((baseMaior * baseMenor) * altura)/2

# Resultado
print("Área do trapézio {}Cm".format(area))