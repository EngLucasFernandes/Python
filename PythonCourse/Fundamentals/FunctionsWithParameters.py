# Funções com parâmetros de entrada

# Funções com parâmetros de entrada são funções que recebem dados para processamento dentro das mesmas

# Entrada -> Processamento -> Saída

def sqrt(number=0):
    return number ** (1/2)


def happy_birthday(name):
    print("Parabéns para você...")
    print("Nesta data querida...")
    print("Muitas felicidades...")
    print("Muitos anos de vida...")
    print(f"Feliz aniversário, {name}!")


happy_birthday("Ada")
