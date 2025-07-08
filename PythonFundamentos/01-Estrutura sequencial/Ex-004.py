'''
 Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
 Autor:Jules do Nascimento Pires
 Ex:004
 Versão:V1
 Data:01/07/2025
'''
# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
n1 = float(input("Primeira nota:"))
p1 = float(input("Primeiro peso:"))
n2 = float(input("Segunda nota:"))
p2 = float(input("Segundo peso:"))
n3 = float(input("Terçeira nota:"))
p3 = float(input("Terçeiro peso:"))

# Limpa a tela
os.system('cls')

# Cálculo da média
media = (n1 * p1 + n2 * p2 + n3 * p3)/(p1 + p2 + p3)

# Mostra o resultado
print("Média aritimética é {}:".format(media, ".2f"))

# Fim