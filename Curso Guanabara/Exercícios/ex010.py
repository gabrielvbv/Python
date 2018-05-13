# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1,00 = R$3,27

d = float(input('Informe quanto dinheiro você tem na carteira: R$ '))
print('Com o valor de R$ {:.2f} você pode comprar US$ {:.2f} dólares.'.format(d, d/3.27))