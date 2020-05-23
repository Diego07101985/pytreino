class A:

    # You want to encapsulate private data on instances of a class,
    # but are concerned about Pythons lack of access control.
    def __init__(self):
        self._internal = 0
        self.__private = 0
        self.public = 1

    def public_method(self):
        print("public_method")
        # A public method
        # An internal attribute
        # A public attribute

    def __internal_method(self):
        print("_internal_method ")

    def __private_method(self):
        print("_private_method")

    # For most code, you should probably just make your nonpublic names start with a single underscore.


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print("_private_method B {0}".format(self.__private))

    def public_method(self):
        print(self.__private_method())


class C(B):
    # O  fato de eu criar um novo method private e uma nova variavel não quer dizer que eu estou subscrevendo o
    # metodo herdado p eu não tenho acesso a ele . O metodo e a variavel criadas ficam invisiveis para as classes que herdam
    # elas
    
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private # Does not override B.__private_method()

    def __private_method(self):
        print("_private_method C {0}".format(self.__private))

    def public_method(self):
        print(self.__private_method())


if __name__ == '__main__':
    a = A()
    a.public_method()
    # eu posso chamar o atributo em tempo de execucao ele nao vai ser bloqueado mas pela convencao
    print(a._internal)

    # o metodo nao pode ser subscrito

    c = C()
    c.public_method()

    # nao deve ser usado
    # utilizado quando eu quero usar um metodo comun em uma classe e utilizar heranca
    a.__internal_method()
