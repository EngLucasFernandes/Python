number_1 = float(input("Digite o primeiro número: "))
number_2 = float(input("Digite o segundo número: "))

if number_1 == number_2:
    print("Os números são iguais!")
elif number_1 > number_2:
    print(f"O número {number_1} é maior que o número {number_2}")
else:
    print(f"O número {number_2} é maior que o número {number_1}")
