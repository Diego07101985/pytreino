l1 = [1, 3, 5, 3, 6, 7, 8, 3, 2]

l2 = [variavel for variavel in l1]

l3 = [v * 2 for v in l1]
l4 = [(v, v1) for v in l1 for v1 in range(3)]

l5 = ['agnes', 'agua']
l6 = [v.replace('a', '@').upper() for v in l5]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex5 = [(x, y) for (x, y) in tupla]

print(dict(ex5))

l7 = [v for v in l1 if v % 2 == 0 if v % 8 == 0]
l8 = [v if v % 2 == 0 else 'abracofree' for v in l1]

print(l7)
print(l8)
# print(l2)
# print(l3)
# print(l4)
# print(l6)
