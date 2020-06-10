# Agregacao uma classe depende da outra pra funcionar corretamente


class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, produto):
        self._produtos.append(produto)

    def lista_produto(self):
        for produto in self._produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        return sum([produto.valor for produto in self._produtos])


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Chinelo', 10)
p3 = Produto('tenis', 500)


carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p2)

carrinho.lista_produto()
print(carrinho.soma_total())
