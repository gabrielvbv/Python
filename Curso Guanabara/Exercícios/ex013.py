# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o seu salário atual?\nR$ '))
print('O seu novo salário, com 15% de aumento, é R${:.2f}'.format(s*1.15))
