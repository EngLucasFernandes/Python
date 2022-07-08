# Métodos são comportamentos que um objeto pode realizar.
# Os métodos são divididos em dois grupos:

# Métodos de Classe e Métodos de Instância


# O método Dunder init (__init__) é o método responsável por construir um objeto a partir de uma classe

# Dunder = Double Underline

# Em Python, os métodos 'Dunder' são chamados de métodos mágicos.

class Lamp:

    brand = "Philips"

    @classmethod
    def get_brand(cls):
        return cls.brand

    def __init__(self, voltage, lumens):
        self.voltage = voltage
        self.lumens = lumens
        self.on = False

    def check(self):
        if self.on:
            print(f"On!")
        else:
            print("Off!")

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False


lampada = Lamp(220, 480)
lampada.check()
lampada.turn_on()
lampada.check()
print(f"Voltage: {lampada.voltage}V")
print(f"Lumens: {lampada.lumens}lm")
print(f"Brand: {Lamp.get_brand()}")

# Métodos de Classe usam um Decorator. O decorator '@classmethod'
