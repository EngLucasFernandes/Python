import time

# Decorators

# Decorators são Higher Order Functions que recebem funções que eles decoram. Exemplo:

def timer(function):
    def get_time():
        start = time.time()
        function()
        end = time.time()
        print(f"Tempo de execução: {end - start}")
    return get_time


@timer
def sum():
    counter = 10
    for number in range(100000000):
        counter += number
    return counter



sum()
