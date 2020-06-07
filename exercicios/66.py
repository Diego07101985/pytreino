carrinho = []

carrinho.append(('Produto 1 ', 30))
carrinho.append(('Produto 2 ', 20))
carrinho.append(('Produto 3 ', 50))


print(carrinho[1])

total = sum([float(value) for produto, value in carrinho])

print(total)
