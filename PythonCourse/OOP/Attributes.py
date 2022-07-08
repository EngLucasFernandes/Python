class Lamp:

    # O método construtor é um método especial, usado para construção dos objetos/instâncias:

    def __init__(self, voltage, color):
        self.voltage = voltage  # Atributo público: 'self.<atributo>'
        self.color = color


class ContaCorrente:

    total_account = 0  # Atributo da classe 'ContaCorrente'

    def __init__(self, balance):
        self.__balance= balance

    def get_number(self):
        print(f"Número da conta: {ContaCorrente.total_account + 1}")
        ContaCorrente.total_account += 1

    def get_balance(self):
        print(f"Valor na conta: R${self.__balance}")

user = ContaCorrente(9000)
user.get_number()
user.get_balance()
user2 = ContaCorrente(5420)
user2.get_number()
user2.get_balance()

print(user.__dict__)  # O atributo '__dict__' lista todos os atributos de uma classe criada.
