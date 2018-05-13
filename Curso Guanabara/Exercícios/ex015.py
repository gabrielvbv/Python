# Escreva um programa que pergunte aa quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

d = float(input('Informe quantos Km o carro percorreu: '))
t = int(input('Informe por qantos dias o carro foi alugado: '))
print('Total a pagar: R${:.2f}'.format(t * 60 + d * 0.15))
