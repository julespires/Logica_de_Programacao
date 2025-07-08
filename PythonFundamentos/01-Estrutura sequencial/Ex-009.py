'''
 Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base * altura)/2.
 Autor:Jules do Nascimento Pires
 Ex:009
 Versão:V1
 Data:03/07/2025
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
base = float(input("Base do triângulo:"))
altura = float(input("Altura do triângulo:"))

# Cálculo da área
area = (base * altura) / 2

# Resultado
print("O triângulo tem uma área de {}cm".format(area))

# Fim