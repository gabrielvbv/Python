# Variáveis usadas nos exemplos
x = 1
y = 2
z = 3

##############################################  SINTAXE BÁSICA  ##############################################

# Para rodar um arquivo python (extensão .py), usamos o terminal escrevendo << python nome_do_arquivo.py >>. Entradas e saidas ocorrerão pelo terminal.

# imprimir um valor:
print ("texto")

# Para escrever um statement em várias linhas, colocamos << \ >> no final da linha:
total = x + \
        y + \
        z

#====================================================================
# Strings podem ser escritas com apostrofe, aspas, ou aspas triplas (''' ou """"), desde que o começo seja igual ao final.
# Aspas triplas são usadas pra escrever textos com parágrafo:
palavra = 'palavra'
frase = "esta é uma frase"
paragrafo = """Este é um parágrafo. O parágrafo será quebrado em duas linhas
para demonstrar como é feito."""

print (palavra)
print (frase)
print (paragrafo)


#====================================================================
# Para darmos espaço entre as linhas, digitamos << \n >> para cada linha que queremos pular:

print ("\n Teste") # pula uma linha
print ("\n\n Teste") # pula duas linhas
print ("\n\n\n Teste") # pula três linhas


##############################################  VARIÁVEIS  ##############################################

# As variávis em Python não precisam de declaração explícita, ou seja, declaração do tipo. O tipo é atribuído automaticamente quando você atribui um valor à ela:

inteiro = 10        # integer
deci = 5.5          # float
nome = "Pafúncio"   # string

# Pode ser atribuido um valor a várias variáveis de uma vez:
a = b = c = 2

# Também podem ser atribuídos valores distintos a variáveis distintas em apenas uma linha:
d, e, f = 1, 2.3, "Moquidésia"

print (d)   # saida: 1
print (e)   # saida: 2.3
print (f)   # saida: Moquidésia

#====================================================================
# O Python tem 5 tipos de dados (data types) padrão, que definem as operações possíveis entre os tipos de variáveis e o método de armazenamento delas:
# Numbers, String, List, Tuple, Dictionary



# NUMBERS - Armazenam valores numéricos, que são:
    # int - inteiros
    # float - "ponto flutuante", com casas decimais
    # complex - números complexos

# É possível deletar a referência a um objeto numérico usando << del >>:
# del var1[,var2[,var3[....,varN]]]]

# Também é possível deletar objetos, apenas um ou vários:
# del var1, var2
# Depois disso as variáveis são excluídas.



# STRINGS - Armazenam sequências de caracteres:
stringue = "Batata"

# Podem ser realizadas algumas operações com strings:
print (stringue)        # imprime a string
print (stringue[0])     # imprime a primeira letra da string
print (stringue[1:5])   # imprime as letras de 2 a 4 da string
print (stringue[2:])    # imprime a string à partir da terceira letra
print (stringue[:5])    # imprime a string até a quinta letra
print (stringue * 2)    # imprime a string duas vezes
print (stringue + " assada")    # concatena as strings



# LISTS - Armazena itens separados por vírgulas entre colchetes, de forma semilar a um array. Todos os itens podem ser de diferentes data types.

lista = ['abc', 550, 2.35, 'Pafúncio', 42, 65, 2.50]
listaMenor = ['def', 330, 'Moquidésia']

# Os itens da lista podem ser acessados usando posições semelhante às de strings:

print (lista)       # imprime a lista completa
print (lista[0])    # imprime o primeiro item da lista
print (lista[1:3])  # imprime do segundo ao trceiro elemento da lista
print (lista[2:])   # imprime todos os elementos a partir do terceiro
print (lista[:4])   # imprime todos os elementos do primeiro ao quinto
print (lista * 2)   # imprime a lista duas vezes
print (lista + listaMenor)  # imprime as duas listas concatenadas

# Um item da lista pode ser atualizado, inclusive mudando o data type:
lista[2] = "Mirosmar Francisco"
print (lista[2])



# TUPLES - Armazena uma sequencia de dados similar à List, separados por vírgulas, mas entre parênteses ao invés de colchetes.
# O acesso aos itens da tupla ocorre da mesma forma que com a lista, a diferença é que uam tupla é considerada como uma lista somente leiura, ou seja, não pode ser alterada.

tupla = ('Antenor', 'Albuquerque', 65)



# DICTIONARY - É um tipo de hash-table (tabela de dispersão, que associa chaves de pesquisa a valores, pra fazer buscas rápidas).
# Funcionam como arrays associativos. Consistem de pares de valores-chave.
# Uma chave do dicionário pode ser de praticamente qualquer tipo, mas normalmente são Numbers ou Strings. Já os valores podem ser de qualquer tipo.

dicionario = {}     # cria um dicionario vazio
dicionario['um'] = "Isso é um"  # cria um item no dicionario com chave "um" e conteudo "Isso é um"
dicionario[2] = "isso é dois"   # chave "2", conteudo "Isso é dois"

dicio = {'nome': 'Pafúncio', 'idade': '23', 'Hobby': 'Videogame'}   # criando um dicionario com tres chaves e valores

print (dicionario)
print (dicio)

dicio['barba'] = True   # adiciona um novo item (chave e valor) no dicionario
dicio['idade'] = 24     #altera o valor da chave "idade"
print (dicio)



# CONVERSÃO DE TIPOS DE DADOS









##############################################  LOOPS  ##############################################


