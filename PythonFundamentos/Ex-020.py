'''
Faça um programa que receba a medida do ângulo (em graus) formado por uma escada apoiada no
chão e encostada na parede e a altura da parede onde está a ponta da escada. Calcule e mostre a me-
dida dessa escada.
Observação: as funções trigonométricas implementadas nas linguagens de programação trabalham
com medidas de ângulos em radianos.
'''

# Bibliotecas
import os
import math

# Limpa a tela
os.system('cls')

# Entrada de dados
angulo = float(input("Medida em ângulo:"))
altura = float(input("Altura da escada:"))

# Cálculo
radiano = angulo * 3.14 / 180
escada = altura / math.sin(radiano)

# Resultado
print("Medida da escada {}".format(escada))