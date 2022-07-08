# Nested Functions

# Em Python, podemos ter declarações de funções dentro de declarações de outras funções. Exemplo:

def math(boolean):
    if boolean:
        def sum(a, b):  # Inner Function (Função interna)
            return a + b
        return sum
    else:
        def dif(a, b):  # Inner Function (Função interna)
            return a - b
        return dif


sum_numbers = math(True)
dif_numbers = math(False)
print(sum_numbers(20, 10))
print(dif_numbers(20, 10))
