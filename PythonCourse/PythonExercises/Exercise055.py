number = float(input("Digite um número: "))

if number >= 0:
    print(f"A raiz de {number} é: {number ** (1/2)}")
else:
    print("Números negativos não tem raiz quadrada no conjunto dos números reais!")
