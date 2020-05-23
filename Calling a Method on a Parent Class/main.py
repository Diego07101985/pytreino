#  You want to invoke a method in a parent class in
#  place of a method that has been overridden in a subclass.


class A:
    def __init__(self):
        self.x = 0

    def spam(self):
        print('A.spam')


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print('B.spam y {0}'.format(self.y))
        print('B.spam x {0}'.format(self.x))
        super().spam()


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    # In this code, the implementation of __setattr__() includes a name check.
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


if __name__ == '__main__':
    b = B()
    b.spam()
