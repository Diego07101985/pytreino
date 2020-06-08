from time import sleep
from time import time


def master(funcao):
    def slave(*args, **kwargs):
        funcao(*args, **kwargs)
        print('Agora estou decorada')
    return slave


@master
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)


outra_funcao('Ola')
# fala_oi()


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo}ms para executar')

        return funcao(*args, **kwargs)
    return interna


@velocidade
def demora():
    for i in range(5):
        sleep(1)


demora()
