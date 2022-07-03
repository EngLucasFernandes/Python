# Usamos o 'for' para iterar sobre sequências ou objetos iteráveis (Tuplas, Listas, Sets, Strings...)

# Exemplos:

name = "Lucas Fernandes"  # Iterável
numbers = [1, 2, 3, 4, 5]

for letter in name:
    print(letter)

for number in numbers:
    print(number)

for number in range(1, 101):  # Em range() o valor final não é incluído!
    print(number)

# Utilizando a função enumerate()

# enumerate() retorna tuplas que contém um índice e um valor associado a esse índice:

# tupla = enumerate(name)

# tupla = (0, "L"), (1, "u"), ...

for i, j in enumerate(name):
    if j != " ":
        print(f"{j} é o {i + 1}º caractere.")
