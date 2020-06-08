from model import Pessoa

pessoa = Pessoa('João', 23)
pessoa.falar("politica")


print(Pessoa.ano_atual)

p1 = Pessoa.por_ano_nascimento("Luiz", 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
