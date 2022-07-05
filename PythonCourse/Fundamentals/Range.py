# A função range() retorna uma sequência de números.

# Sintaxe:

# range(<início>, <fim>, <passo>)  - O último número não é incluído!

# Exemplos:

numbers = list(range(10))  # Números de 0 a 9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    print(number)

numbers = list(range(10, 0, -1))  # Números de 10 a 1

for number in numbers:
    print(number)
