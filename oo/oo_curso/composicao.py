# na composicao uma classe pertence a outra classe


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self._enderecos = []

    def insere_endereco(self, cidade, estado):
        self._enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self._enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


cliente1 = Cliente('Luiz', 23)
cliente1.insere_endereco('Salvador', 'BA')
cliente1.insere_endereco('Rio de Janeiro', 'RJ')
cliente1.lista_enderecos()

print()

cliente2 = Cliente('João', 43)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.lista_enderecos()
