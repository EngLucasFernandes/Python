# Uma string é uma sequência de caracteres alfanuméricos.
# Tudo entre aspas simples, aspas duplas, aspas simples triplas ou aspas duplas triplas são strings.

# Exemplos:

name = "Lucas Fernandes"
country = "Brazil"
string_number = "123"

# Strings são estruturas indexadas, ou seja, é possível acessar um determinado caractere a partir de um índice.

print(name[0])  # Imprime o primeiro caractere de 'name'

# Usando Slice Strings

print(name[0:5])  # Imprime do primeiro caractere de 'name' até o quinto caractere.

print(string_number[2])

# Métodos úteis para strings:

# upper() -> Converte todos os caracteres de uma string para caracteres maiúsculos.
# lower() -> Converte todos os caracteres de uma string para caracteres minúsculos.
# split() -> Divide uma string em uma lista com strings.
# replace(a, b) -> Substitui 'a' por 'b' em uma string.
