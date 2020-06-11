

class A:
    # def __new__(cls, *args, **kwargs):

    #     if not hasattr(cls, '_jaexiste'):
    #         cls._jaexiste = object.__new__(cls)

    #     return cls._jaexiste
    #     # return object.__new__(cls)
    #     # return super().__new__(cls)

    # def __init__(self):
    #     print('Eu sou o Init')

    # def __setattr__(self, name, value):
    #     self.__dict__[name] = value
    #     print(name, value)

    def __del__(self):
        print('Objeto Coletado')

    def __str__(self):
        return 'Class <A>'
    # def __call__(self, *args, **kwargs):
    #     resultado = 1
    #     for i in args:
    #         resultado *= i
    #     return resultado


a = A()
a.nome = 'Luiz Otavio'
print(a)
# variavel = a(1, 2, 3, 4, 5, 6, 7)
#  b = A()
# c = A()


# print(variavel)
# # print(b)
# print(c)
