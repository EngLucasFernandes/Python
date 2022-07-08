# Módulos Built-In (Módulos que já vem instalados no Python)

# Existem mais de 200 módulos Built-In em Python

# Utilizando 'alias' (apelidos):

# Sintaxe:

# from <módulo> import <função> as <apelido> 

# Exemplos:

from random import randint as rdt, random as rdm


print(rdt(0, 10))
print(rdm(0, 10))

# Importando todas as funções de um módulo:

from random import *
