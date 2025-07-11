'''
Escreva um programa para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto 
pessoas cujo salário é maior que R$ 1.200,00.
'''

import os

os.system('cls')


salario = float(input("Qual é o seu salário atual? R$:"))

if salario > 1200:
    print('*' * 70)
    print("O seu salário é R$ {:.3f}, você deverá pagar imposto de renda!".format(salario))
    print('*' * 70)

else:
    print('*' * 70)
    print("O seu salário é R$ {:.3f}, você não precisa pagar imposto de renda!".format(salario))
    print('*' * 70)