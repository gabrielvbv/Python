#Crie um script Python que leia dois números e tente mostrar a soma entre eles.

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
print('A soma é', n1 + n2)

# Após explicação de máscara, e adicionando uma variável pra soma:

soma = n1 + n2
print('A soma de {} e {} é igual a {}'.format(n1, n2, soma))

#também pode-se usar números dentro das máscaras pra facilitar na leitura, e que não alteram em nada no resultado
print('A soma de {0} e {1} é igual a {2}'.format(n1, n2, soma))