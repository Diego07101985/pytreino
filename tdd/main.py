from calculo import somar


try:
    print(somar(12, '232'))
except AssertionError as err:
    print(f'conta invalida {err}')


print(somar(12, 232))
