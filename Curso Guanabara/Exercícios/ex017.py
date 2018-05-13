# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Obs: usar a biblioteca "math"

from math import hypot  # hypot - hipotenusa. Calcula a hiptenusa de acordo com os parâmetros dos catetos.

print('Informe abaixo o comprimento dos catetos de um triângulo retângulo:')
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('Dados cateto oposto = {:.2f} e cateto adjacente = {:.2f}, a hipotenusa mede {:.2f}.'.format(co, ca, hypot(co, ca)))
l