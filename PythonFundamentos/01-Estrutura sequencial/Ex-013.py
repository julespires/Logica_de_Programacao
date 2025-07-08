'''
Sabe-se que:
pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1,760 jarda
Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
a) polegadas;
b) jardas;
c) milhas.
Autor:Jules do Nascimento Pires
Ex:013
Versão:V1
Data:04/07/2025
'''


# Biblioteca 
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
pes = float(input("Digite uma medida em pés:"))

# Cálculos
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760

# Resultados
print("{} pés é igual a {} polegadas ".format(pes, polegadas)) 
print("{} pés é igual a {} jardas ".format(pes, jardas)) 
print("{} pés é igual a {} milhas ".format(pes, milhas)) 

# Fim