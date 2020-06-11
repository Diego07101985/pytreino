from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando...B... ')


class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def conta(self):
        return self._conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo Precisa ser numérico')
        self._saldo = valor

    def detalhes(self):
        print(f'Agencia : {self._agencia}')
        print(f'Conta  : {self._conta}')
        print(f'Saldo : {self._saldo}')

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo Precisa ser numérico')
        self._saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo Insuficiente')
            return

        self._saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def detalhes(self):
        print(f'Agencia : {self._agencia}')
        print(f'Conta  : {self._conta}')
        print(f'Saldo : {self._saldo}')

    def sacar(self, valor):
        if self._saldo+self._limite < valor:
            print('Saldo Insuficiente')
            return
        self._saldo -= valor
        self.detalhes()


a = B()
a.falar()


# c1 = ContaPoupanca(1111, 2222, 0)
# c1.depositar(10)
# c1.sacar(5)
# c1.sacar(5)
# c1.sacar(5)

c2 = ContaCorrente(111, 23232, 0)
c2.depositar(20)
c2.sacar(5)
c2.sacar(5)
c2.sacar(5)
c2.sacar(5)
