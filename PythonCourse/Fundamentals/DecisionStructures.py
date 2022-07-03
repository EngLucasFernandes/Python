# Estruturas de decisão: if, if ... else, if ... elif ...

idade = int(input("Digite a sua idade: "))

# Se uma condição é verdadeira, então é executado um determinado bloco de código

if idade < 18:
    print("Menor de idade!")  # Bloco de código 001
elif idade == 18:
    print("Você tem exatamente 18 anos de idade!")  # Bloco de código 002
else:
    print("Maior de idade!")  # Bloco de código 003
