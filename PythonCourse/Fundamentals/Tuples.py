# Tuplas assim como listas, são coleções/sequências ordenas de itens/elementos. Entretanto, são imutáveis, ou seja,
# não permitem a alteração da tupla depois da declaração/inicialização da tupla. Toda alteração em uma tupla, gera uma
# nova tupla.

inteiros = (1, 2, 3)
print(type(inteiros))  # Retorna 'tuple'
print(inteiros)

novos_inteiros = (-3, -2, -1, 0) + inteiros
print(novos_inteiros)

# As tuplas também, assim como as listas, aceitam quaisquer tipos de dados:

nova_tupla = (1, 3.14, "Python", True, [1, 2, 3], (19, 20, 21))

# Tuplas só têm dois métodos:

# count() e index()

# count() - O método count() conta o número de ocorrências de um determinado valor:

print(nova_tupla.count("Python"))

# index() - O método index() indica o índice de um item específico:

print(nova_tupla.index(3.14))

# CUIDADO: Para representar tuplas com apenas um elemento, devemos usar vírgula após o item:

numero = 4  # Número inteiro
tupla = (4, )  # Tupla de um único elemento

# Tuplas sem parênteses

number = 4,  # Tupla
numbers = 1, 2, 3, 4  # Tupla

tpl = tuple(range(0, 100))

# Desempacotamento de tuplas

name = ("Python", "Training",)
language, action = name
print(language)
print(action)

# Também é possível utilizar, em tuplas, as funções:

# sum(), max(), min(), len()
