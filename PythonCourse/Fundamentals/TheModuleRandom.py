# Módulos são arquivos Python que contém definições/códigos que podem ser acessados e usados em
# outros arquivos Python

# Importando todo o módulo 'random' (Não recomendado):

import random

# O módulo random possui inúmeras funções para geração de números pseudo-aleatórios.

# Utilizando uma função de um pacote:

# Sintaxe:

# <módulo>.<função>()

random_number = random.randint(0, 10)
print(f"The random number is {random_number}")

# Se quiser importar funções específicas, use a sintaxe:

# from <módulo> import <função>, <função> ...

# Exemplo:

from time import sleep, time

start = time()
sleep(10)
end = time()
total = end - start
print(total)
