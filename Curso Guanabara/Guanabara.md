##### 04 - Primeiros comandos
Mensagens são usadas primordialmente pra serem exibidas na tela, números pra fazer operações. Mensagens devem estar entre delimitadores, numeros sozinhos não, que podem ser aspas simples ou duplas. O mais comum é usar aspas simples.

    print('Hello, world!')  - A mensagen Hello World aparece na tela
    print(7+4)              - O resultado da conta aparece na tela
    print('7'+'4')          - Os números concatenados (74) aparece na tela, e não é um número, é uma mensagem

Pra concatenar uma mensagem com um número usamos vírgula ao invés do sinal de +
    print('Resultado:' + 5)        ERRO
    print('Resultado:', 5)         Imprime a mensagem corretamente

========================================

$$$ Variáveis

No python, toda variável é um objeto. Não é necessário declarar tipo, ele se define pelo valor atribuido.

    nome = 'Pafúncio'   - String
    idade = 30          - Int
    altura = 1.75       - Float

    print(nome, idade, peso)    - nesse caso, usar o + não funcionaria, tem que ser com vírgulas pois mistura mensagem com número.


Solicitando valores para o usuário - utilizamos INPUT

    nome = input('Informe seu nome: ')
    idade = input('Informe sua idade: ')
    altura = input('informe sua altura: ')
    printm(nome, idade, peso)


EXERCÍCIOS: 1 E 2

##### 06 - Tipos primitivos

O Python tem 4 tipos primitivos fundamentais:

    int - inteiro
    float - ponto flutuante, números real, ou seja, número com casas decimais
    str - string, palavras, vetor de caracteres. Representado sempre entre aspas.
    bool - Booleano, 'verdadeiro' e 'falso', True / False (sempre com a primeira letra maiuscula)

Obs: '' é uma string vazia

Nova forma de realizar o print com variáveis:
    print('A soma vale {}'.format(soma))
Colocamos as chaves, que é uma máscara, e usamo um método de qualquer string, que é o .format. Dentro de .format colocamos o que via aparecer na máscara.

**Essa sintaxe só existe à partir do Python 3


Podemos verificar o tipo de um valor usando << type >>
    print(type(n1)) - Imprime o tipo da variável

Podemos definir o tipo de um input usando os tipos primitivos, por exemplo:

    n1 = int(input('Digite um número: ))

Quando imprimimos um float, se o valor for inteiro, ele mostra com .0 no final pra indicar que é float. Por exemplo:
    n = float(4)
    print(n)        - resultado: 4.0

Quando fazemos algo semelhante com << bool >>, ele sempre mostra TRUE quando entramos com algum valor na variável, e se ela fica vazia ele vai atribuir FALSE


$$$ Alguns métodos:

Como toda variável é um objeto, toda variável tem métodos.

isnumeric() = retorna se o valor é numérico ou não, independente do tipo primitivo. Por exemplo:
    n = input('Digite algo: )
    print(n.isnumeric())
Se digitamos 'oi' o retorno é FALSE
Se digitamos '4' o retorno é TRUE
Nos dois casos o que foi digitado é uma string, mas o 4, apesar de string, é numérico. Ele diz, nesse caso, se é possível converter o valor que estamos testando em um tipo primitivo int ou float.

    .isalpha()  - diz se é alfabético
    .isalnum()  - diz se é alfanumérico
    .usupper()  - diz se tudo está em letrar maiúsculas
Existem muitos .isALGUMACOISA(), que são métodos de teste de tipo.

Alguns outros:
    .isnumeric()    - diz se é numérico
    .isspace()      - diz se todos os caracteres são espaço


EXERCÍCIOS: 3 E 4

##### 07 - Operadores aritméticos

+ → adição
- → subtração
* → multiplicação
/ → divisão
** → potência
// → divisão inteira
% → módulo (resto da divisão)

Todo operador precisa de operandos, que pode ser um número, string, ou variáves.
Todos são operadores vinários, então precisam de dois operandos.
Ao testar se uma coisa é igual a outra, usa-se == para comparação.

--Ordem de precedência:
1 - () parênteses
2 - ** potências
3 - * / // % (tendo todos "juntos", ele resolve quem aparecer primenro)
4 - + -

Em python ele não tem limite de tamanho nas variáveis, diferente de outras linguagens (como Java).

Também podemos fazer a potenciação com o método <<pow(x,y)>>, sendo x a base e y o expoente

Pra fazer raiz quadrada podemos elevar ao inverso, por exemplo:
raiz de 81 → 81**(1/2)
raiz cubica de 125 → 125**(1/3)

Também é possível usar os operadores com strings, como a concatenação já vista. Exemplos:
    'Bom '+'dia!'   → 'Bom dia!'
    '='*20          → '===================='

É possível escrever strings em uma determinada quantidade de caracteres predefinida, independente do tamanho da String. Por exmeplo:
print('Olá {}!'.format(nome))    → Olá Fulano!
Em 20 espaços:  print('Olá {:20}'.format(nome)) → Olá Fulano              !
Alinhado à esquerda:  {:<20}  → Olá Fulano              !
Alinhado à direita:   {:>20}  → Olá               Fulano!
Centralizado:         {:^20}  → Olá        Fulano       !
Centralizado com caracteres complementares: {:=^20} → Olá =======Fulano=======!

--Formatando variáveis float:
Para formatar um resultado para uma quantidade determinada de casas após a vírgula, fazemos a formatação dentro dos colchetes:
    print('A divisão é: {:.2f}'.format(divisao))
.2 indica que são duas casas após a vírgula, f indica que é float.

É possível fazer dois ou mais prints sem mudar de linha, colocando o seguinte termo no final do print (depois do format também, caso ele esteja sendo usado):
    , end=''
Dentro desse end podemos colocar o que será o final, mas de qualquer forma o final não vai ser pular para uma nova linha (caractere enter, "\0"), então podemos colocar algum caractere, mais espaços, etc.
Pra pular linhaem um print só, colocamos << \n >>, no meio do texto.



***não foi passado, mas complementando
pra continuar escrevendo uma linha na linha de baixo, colocamos \ no final da linha


EXERCÍCIOS: 5 AO 13
14 e 15 extra, não foi dado o enunciado na aula.

##### 08 - Utilizando Módulos

O Python trabalha com módulos, que extendem as possibilidades além do básico que vem com a linguagem. Esses módulos podem ser importados quando forem necessários.
O módulo é chamado de biblioteca.

Para importar uma biblioteca, usamos IMPORT e o nome da biblioteca:
    import bebidas
Se não precisarmos importar toda a biblioteca, mas apenas um método (função) dela, fazemos:
    from bebidas import refrigerante
Dessa forma ele só importa no programa o método refrigerante.

A diferença entre essas duas formas é que na primeira, para usar o método é necessário digitar:
    bebidas.refrigerante()
e da segunda forma só é necessário:
    refrigerante()
Inclusive, importando da segunda forma não é possível utilizar "bebidas", pois a biblioteca não foi importada, apenas o método "refrigerante" foi.


Uma biblioteca muito usada é a MATH, e aqui alguns exemplos de funcionalidades:
    ceil - arredonda pra cima
    floor - arredonda pra baixo
    trunc - trunca o número, elimina o que ta depois da virgula
    pow - potenciação
    sqrt - raiz quadrada
    factorial - fatorial e um número

Pra importar mais de uma funcionalidade e ainda assim não importar a biblioteca inteira, colocamos o nome das funcionalidades separados por vírgulas:
    from math import sqrt, ceil

No site do Python, python.org, tem uma lista de pacotes em PyPI (Python Package Index), que mostra uma lista bem extensa de pacotes que podem ser baixados e adicionados ao Python.
Também é possível criar uma biblioteca e disponibilizá-la para a comunidade.

*Usado na resolução do exercício 19: LIST
Uma lista contém vários itens, por exemplo:
lista = ['a', 'b', 'c']
A lista deve sempre estar entre colchetes, e elementos string são armazenados sempre com aspas simples.

EXERCÍCIOS: 16 AO 21

