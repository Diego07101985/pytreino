import sys
import time

lista = [0, 1, 2, 3, 4, 5, 6]

print(hasattr(lista, '__iter__'))


lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))


lista = list(range(100))

print(sys.getsizeof(lista))


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))


def get_iterators():
    variavel = "texto1"
    yield variavel
    variavel = "texto2"
    yield variavel
    variavel = "texto3"
    yield variavel


v = get_iterators()
print(next(v))
print(next(v))
print(next(v))
# print(next(v))
# print(next(v))


l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

print(l2)

# for v in l2:
#     print(v)


nome = "Luiz Otavio"

iterador = iter(nome)

gerador = (letra for letra in nome)


print(next(gerador))
