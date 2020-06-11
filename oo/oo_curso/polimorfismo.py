from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def escrever(self, word):
        pass


class B(A):
    def escrever(self, word):
        print(f'Escrever B {word}')


class C(A):
    def escrever(self, word):
        print(f'Escrever C {word}')


b = B()


b.escrever("abraco")
