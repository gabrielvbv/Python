# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle  # shuffle embaralha a ordem dos elementos de uma lista

alunos = []
print('Informe o nome dos alunos:')
alunos.append(str(input('Aluno 1: ')))  # append é o equivalente ao PUSH de outras linguagens, coloca um item no final da lista.
alunos.append(str(input('Aluno 2: ')))
alunos.append(str(input('Aluno 3: ')))
alunos.append(str(input('Aluno 4: ')))

shuffle(alunos)

print('Ordem de apresentação dos trabalhos:\n\
    1° -> {}\n\
    2° -> {}\n\
    3° -> {}\n\
    4° -> {}\
    '.format(alunos[0], alunos[1], alunos[2], alunos[3]))

# Na resolução do exercício foram atribuidos os nomes a 4 variáveis, que depois foram atribuidas a uma lista de 4 elementos, antes de usar o shuffle.
'''
    a1 = str(input('Aluno 1: '))
    a2 = str(input('Aluno 2: '))
    a3 = str(input('Aluno 3: '))
    a4 = str(input('Aluno 4: '))
    lista = [a1, a2, a3, a4]
    shuffle(lista)
'''