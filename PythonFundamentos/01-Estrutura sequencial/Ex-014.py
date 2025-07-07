'''
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa;
b) quantos anos ela terá em 2050.
'''

# Bibliotecas
import os
from datetime import date

# Limpa a tela
os.system('cls')
anoNascimento = int(input("Ano de nascimento:"))

# Calcula a idade atual e em 2050
idadePessoa = date.today().year - anoNascimento
id2050 = 2050 - anoNascimento

# Resultado
print("Sua idade atual é {} anos em 2050 você terá {} anos".format(idadePessoa, id2050))
