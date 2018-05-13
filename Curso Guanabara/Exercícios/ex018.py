# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Obs: usar a biblioteca "math" ou outra que facilite.

from math import radians, sin, cos, tan


a = float(input('Informe a medida de um ângulo: '))
print('Dado o ângulo {}:\n\
    Seno -> {:.2f}\n\
    Cosseno -> {:.2f}\n\
    Tangente -> {:.2f}\
    '.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))

# É necessário converter o ângulo para radianos pois o parâmetros das funções sin() cos() e tan() está em radianos, não em graus)
# Informação disponível em https://docs.python.org/3/library/math.html#trigonometric-functions