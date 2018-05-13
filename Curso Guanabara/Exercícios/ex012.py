# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Informe o preço do produto: R$ '))
print('O novo preço com 5% de desconto é R$ {:.2f}'.format(p*0.95))