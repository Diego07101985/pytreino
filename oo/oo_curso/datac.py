from dataclasses import dataclass


@dataclass(order=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo invalido {type(self.nome).__name__}!= str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('A', '1')
p2 = Pessoa('B', '3')
p3 = Pessoa('C', '2')
p4 = Pessoa(122121, '4')

# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo)

# print(p1 == p2)

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
