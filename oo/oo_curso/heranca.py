''''
Associação - Usa | Agregacao - Tem | Composicao - é dono | Heranca - é um
'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando')


c1 = Cliente('Agnes', 26)
c1.falar()
a1 = Aluno('Diego', 26)
print(a1.nome)
a1.falar()
