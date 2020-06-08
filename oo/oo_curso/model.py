class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade, falando=True):
        self.nome = nome
        self.idade = idade
        self.falando = falando

    def falar(self, assunto):
        print(f'Esta {self.nome} sobre {assunto}')
        self.falando = True

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
