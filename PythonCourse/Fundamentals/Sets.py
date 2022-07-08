# Sets (Conjuntos)


# Adicionando elementos em um Set:

conjunto_naturais = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"Conjunto dos números naturais antes da adição: {conjunto_naturais} \n")
conjunto_naturais.add(4)  # Informamos o valor a ser adicionado
print(f"Conjunto dos números naturais depois da adição: {conjunto_naturais} \n")

# Removendo elementos em um Set:

conjunto_naturais = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"Conjunto dos números naturais antes da subtração: {conjunto_naturais} \n")
conjunto_naturais.remove(9)  # Informamos o valor a ser removido
print(f"Conjunto dos números naturais depois da subtração: {conjunto_naturais} \n")

print(f"Conjunto dos números naturais antes da subtração: {conjunto_naturais} \n")
conjunto_naturais.discard(10)  # Informamos o valor a ser descartado (RECOMENDADO)
print(f"Conjunto dos números naturais depois da subtração: {conjunto_naturais} \n")

# Copiando conjuntos:

# Deep Copy

print("Deep copy: ")
novo_conjunto = conjunto_naturais.copy()
print(id(novo_conjunto))
print(id(conjunto_naturais), "\n")

# Shallow Copy

print("Shallow copy: ")
outro_conjunto = conjunto_naturais
print(id(outro_conjunto))
print(id(conjunto_naturais), "\n")

# Limpando todos os elementos de um Set
outro_conjunto.clear()
print(outro_conjunto)

# Operações com conjuntos

# União

conjunto_naturais = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_racionais = {1.2, 1, 2.3, 3, 3.4, 4.5, 5.6, 6.7, 7, 7.8, 8.9, 9.1}
conjunto_reais = conjunto_racionais.union(conjunto_naturais)
print(f"Conjunto dos números reais: {conjunto_reais}")

# Interseção

print(f"Conjunto dos números naturais no conjunto dos números racionais: {conjunto_naturais.intersection(conjunto_racionais)}")

# Diferença

print(conjunto_racionais.difference(conjunto_naturais))
print(conjunto_reais.difference(conjunto_racionais))
