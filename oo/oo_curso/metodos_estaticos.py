from random import randint


class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade, falando=True):
        self.nome = nome
        self.idade = idade
        self.falando = falando

    # def falar(self, assunto):
    #     print(f'Esta {self.nome} sobre {assunto}')
    #     self.falando = True

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


print(Pessoa.ano_atual)

p1 = Pessoa.por_ano_nascimento("Luiz", 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
