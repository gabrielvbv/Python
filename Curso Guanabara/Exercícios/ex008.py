# Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.

v = float(input('Digite um valor em metros: '))
print('{:.2f} metros é igual a {:.2f} centímetros e {:.2f} milímetros'.format(v, v*100, v*1000))
