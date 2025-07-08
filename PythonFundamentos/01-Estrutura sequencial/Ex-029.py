'''
Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, consi-
derando peso 2 para a primeira e peso 3 para a segunda.
Autor:Jules do Nascimento Pires
Ex:029
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))

# Cálculo da média ponderada
media = (nota1 * 2 + nota2 * 3) / (2 + 3)

# Resultado
print("A média ponderada entre {} e {} = {}".format(nota1, nota2,media))

# Fim