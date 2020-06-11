
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.nomeclasse = self.__class__.__name__

    def falar(self):
        print("Pessoa")


class Cliente(Pessoa):
    def comprar(self):
        print('Cliente')

    # def falar(self):
    #     print("CLiente fala")


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')


c1 = ClienteVip('Agnes', 26, 'Souza')
c1.falar()
# c1.comprar()
