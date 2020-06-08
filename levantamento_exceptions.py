# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('Log:', error)
#         raise


def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1/n2


try:
    print(divide(2, 0))
except ValueError as error:
    print(error)


def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um numero '))
    if numero is None:
        print('Isso não é um numero')
    else:
        print(numero*5)
