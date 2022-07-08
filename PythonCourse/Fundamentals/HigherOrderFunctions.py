# Higher Order Functions

# Higher Order Functions são funções que recebem uma ou mais funções como argumentos ou retornam
# uma ou mais funções.

# Exemplo:

def sum(a, b):
    return a + b


def calc(a, b, function):  # Higher Order Function
    return function(a, b)


# A função 'calc' é uma Higher Order Function, pois recebe como argumento, a função 'sum'

print(calc(5, 10, sum))
