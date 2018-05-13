# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira (o valor sem o decimal).
# Obs: usar a biblioteca "math"

from math import trunc  # trunc - truncate, vai deixar só a parte inteira do número.

n = float(input('Informe um número real: '))
print('A porção inteira de {} é {}'.format(n, trunc(n)))

# Feedback da resolução:
# Também é possível fazer sem importar nada, substituindo trunc(n) por int(n)
