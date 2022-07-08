# Decorators com diferentes assinaturas

def gritar(function):
    def aumentar(name):
        return function(name).upper()
    return aumentar


@gritar
def greetings(name):
    return f"Olá, eu sou {name}."

print(greetings("Lucas"))
