'''
Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que
o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir para
atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem
estar em metros.
Autor:Jules do Nascimento Pires
Ex-019
Versão:V1
Data:06/07/2025
'''

# Biblioteca usada
import os

os.system('cls')

# Entrada de dados
alturaDegrau = float(input("Informe a altura do degrau:"))
alturaSubir = float(input("Informe a altura que o usuário deseja subr:"))

# Cálculo
quantidadeDegrau = alturaSubir / alturaDegrau

# Resultado
print("Para atingir seu objetivo, deverá subir {} degraus".format(quantidadeDegrau))