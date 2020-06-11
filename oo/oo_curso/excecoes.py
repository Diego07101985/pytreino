class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('erro')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')
