"""
# Métodos úteis para listas

# sort() - Ordena uma lista

integers.sort()  # A lista 'integers' foi ordenada
print(integers)

# count() - Conta o número de ocorrências de um determinado item em uma lista

print(integers.count(9))

# Concatenando listas

numbers = integers + float_numbers  # Faz a mesma coisa que o método extend()
print(numbers)

# reverse() - Inverte os elementos de uma lista

integers.reverse()  # Invertendo
print(integers)
integers.reverse()  # Voltando ao estado normal da lista

# É possível também...
print(integers[::-1])

# copy() - Copiando os valores de uma lista para outra

new_integers = integers.copy()
print("=" * 100)
print(new_integers)

# Função len() - A função len() retorna o tamanho de um iterável
print(len(new_integers))

"""

# As listas em Python são coleções/sequências ordenadas de itens/elementos:

lista = [1, 2, 3, 4, 5]  # Uma lista contendo alguns números inteiros.
nomes = ["Lucas", "Daniel", "João", "Pedro"]  # Uma lista contendo algumas strings.
lista_personalizada = [1, 3.5, True, "Python", [1, 2, 3]]  # Uma lista contendo diferentes tipos de dados

# Listas podem conter elementos de tipos diferentes.
# Podem até mesmo ter listas, tuplas, dicionários ou sets dentro delas:

lista_nova = [[1, 2, 3], (1, 2, 3), {1: "Um", 2: "Dois", 3: "Três"}, {1, 2, 3}]

# Os elementos em uma lista podem ser acessados através de um índice, pois todos os elementos em uma lista estão
# associados a um índice.

print(lista[2])  # Imprimirá o valor '3' na tela.

print(lista[0:2])  # Imprimirá a lista '[1, 2, 3]' na tela.

# Adicionando elementos a uma lista usando métodos:

# append() -  O método append() adiciona um elemento a última posição em um lista:
lista.append(6)  # A lista agora é: [1, 2, 3, 4, 5, 6]

# insert() - O método insert() insere um elemento em uma posição específica em uma lista:
lista.insert(0, -1)  # A lista agora é: [-1, 1, 2, 3, 4, 5, 6]

# extend() - O método extend() concatena uma lista e um objeto iterável qualquer:
lista.extend(nomes)  # A lista agora é [-1, 1, 2, 3, 4, 5, 6, "Lucas", "Daniel", "João", "Pedro"]

# remove() - O método remove() remove um item específico de uma lista:

inteiros = [1, 2, 3, 7, 4]
inteiros.remove(7)
print(inteiros)

# pop() - O método pop(), por padrão, remove o último elemento de uma lista e o retorna/devolve:

inteiros = [1, 2, 3]
popped_number = inteiros.pop()
print(f"Lista: {inteiros} \t Número retirado: {popped_number}")

# clear() - O método clear() limpa todo o conteúdo de uma lista:

lista = [1, 2, 3, 4]
lista.clear()
print(lista)

# A palavra reservada 'del' pode remover um elemento específico em uma lista:

lista = [1, 2, 3, 4, 5, 6, 7]
del lista[0]
print(lista)

# Ou também deletar uma lista por completo:

del lista

# Iterando sobre listas:

numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    print(number)

[print(number) for number in numbers]
