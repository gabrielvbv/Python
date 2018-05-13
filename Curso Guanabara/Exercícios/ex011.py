# faça um programa que leia a largura e a altura de uma parede em metros, e calcule sua área e a quantidade de tinta necessária para pintá-la.
# Considere que cada litro de tinta pinta uma área de 2m².

l = float(input('Informe a largura da parede (em metros): '))
h = float(input('Informe a altura da parede (me metros): '))
a = l * h
print('Área da parede: {:.2f}m²  //  Tinta necessária: {}L'.format(a, a/2))