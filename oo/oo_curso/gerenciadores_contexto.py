from contextlib import contextmanager


# class Arquivo:
#     def __init__(self, arquivo, modo):
#         print('init')
#         self.arquivo = open(arquivo, modo)

#     def __enter__(self):
#         print('enter')
#         return self.arquivo

#     def __exit__(self, exec_type, exec_val, exec_tb):
#         print('sair')
#         self.arquivo.close()
#         print(exec_type)
#         print(exec_val)
#         print(exec_tb)


# with Arquivo('abc.txt', 'w') as arquivo:
#     arquivo.write('alguma coisa')


@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('Abrindo')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
