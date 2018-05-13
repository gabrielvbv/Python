# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# Obs: tem uma biblioteca random

from random import choice   # "Choice" é um método de random que deixa escolher um tem aleatório de uma lista.

print('Informe o nome dos alunos:')
a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))
print('{} foi o escolhido para apagar o quadro!'.format(choice([a, b, c, d])))
