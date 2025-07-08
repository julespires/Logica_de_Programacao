'''
Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma. 
Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.
Autor:Jules do Nascimento Pires
Ex:018
Versao:V1
Data:05/07/2025
'''

# Biblioteca usada
import os

# Limpa a tela do prompt
os.system('cls')

#Entrada de dados
pesoSaco = float(input("Informe o peso do saco de ração:"))
racaoGato1 = float(input("Informe a quantidade ração do primeiro gato:"))
racaoGato2 = float(input("Informe a quantidade ração do segundo gato:"))

# Área do cálculo
racao1 = racaoGato1 / 1000
racao2 = racaoGato2 / 1000
totalFinal = pesoSaco * 5 (racaoGato1 + racaoGato2)


# Resultado
print("O restante de ração no saco após 5 dias será de {}".format(totalFinal))

3 # Fim