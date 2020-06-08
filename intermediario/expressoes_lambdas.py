def a(x, y): return x * y


print(a(2, 3))


lista = [
    ['P1', 12],
    ['P2', 6],
    ['P3', 7],
    ['P4', 8]
]


def func(item):
    return item[1]


lista.sort(key=func, reverse=True)
lista.sort(key=lambda item: item[1])
print(sorted(lista, key=lambda item: item[1]))

print(lista)
