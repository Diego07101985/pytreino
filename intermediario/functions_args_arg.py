

def func(*args, **kwargs):
    print(kwargs)
    lista = list(args)
    lista[0] = 20
    print(lista)


def func2(*args, **kwargs):
    print(args)
    idade = kwargs['idade']

    if idade is not None:
        print(idade)


lista = [1, 2, 3, 4, 5]
# n1, n2, *n = lista
# print(f'N1 = {n1} ,n2=  {n2} ,*n = {n}')
# print(*lista, sep='-')

# func(*lista, 10, 2, 3, 5, nome="amor", tipo="abraco")

func2(*lista, idade=122)

