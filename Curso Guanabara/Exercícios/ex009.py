# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# Como foi solicitado, pra fazer apenas com o que foi dado em aula até o momento:

n = int(input('Digite um número inteiro: '))
print('Tabuada do número {0}:\n\
    {0} x 1 = {1}\n\
    {0} x 2 = {2}\n\
    {0} x 3 = {3}\n\
    {0} x 4 = {4}\n\
    {0} x 5 = {5}\n\
    {0} x 6 = {6}\n\
    {0} x 7 = {7}\n\
    {0} x 8 = {8}\n\
    {0} x 9 = {9}\n\
    {0} x 10 = {10}\n\
    '.format(n, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))

########################################################

# Da forma mais prática, com if: