# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
# 1.8 * tempC + 32

t = float(input('informe a temperatura em °C: '))
print('A temperatura de {:.1f}°C é igual a {:.1f}°F'.format(t, t * 1.8 + 32))
