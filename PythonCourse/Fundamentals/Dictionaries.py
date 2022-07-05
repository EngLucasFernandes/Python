# Dicionários (Ou mapas, em outras linguagens de programação)são também coleções/sequências de elementos.

# Entretanto cada elemento/valor (value) está associado à uma chave (key).

# NÃO podemos ter chaves repetidas!

# Exemplo

countries = {"BR": "Brazil", "UK": "United Kingdom", "JP": "Japan"}
print(countries)
print(type(countries))

# Os elementos em dicionários também podem ser de diferentes tipos. As chaves também podem ter um tipo diferente do
# valor associado:

dictionary = {"First item": 1, "Second item": 1.5, "Third item": True, "Forth item": "String", "Fifth item": [1, 2]}

# Acessando elementos - Usando chaves:

print(countries["BR"])

# Acessando elementos - Usando  o método get() (Recomendado)

print(countries.get("BR"))
print(countries.get("RU"))  # Se for passada uma chave inexistente, 'None' é retornado.

# É possível checar se uma chave está contida em um dicionário:

# user_country = input("Digite a sigla do seu país: ").upper()
#
# if user_country in countries:
#     print(f"País encontrado: {countries.get(user_country)}")
# else:
#     print("País não encontrado!")

# Sintaxe: <chave> in <dicionário>

# Adicionando elementos em um dicionário (Forma 1):

countries["UK"] = "Ukraine"  # Se a chave já estiver no dicionário, o valor será modificado
# Se a chave não estiver no dicionário, um novo valor será criado e atribuído à essa chave.

# Adicionando elementos/ atualizando elementos em um dicionário usando o método update():

iterable = {"PY": "Paraguay"}
countries.update(iterable)
print(countries)

countries.update({"PY": "Python"})
print(countries)

# Removendo um elemento usando o método pop()

popped_country = countries.pop("UK")
print(popped_country)

# Removendo um elemento usando a palavra reservada 'del':

del countries["PY"]
print(countries)

# Copiando dicionários usando o método copy()

new_countries = countries.copy()  # Deep Copy

countries_2 = countries  # Shallow Copy (Cópia por referência)

# Criando dicionários usando outros iteráveis:

new_dictionary = {}
new_dictionary = new_dictionary.fromkeys("??", "Sem valor")
print(new_dictionary)
