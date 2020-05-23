# Although this “works” for most code, it can lead to bizarre trouble
# in advanced code involving multiple inheritance.

# If you run this code, you’ll see that the Base.__init__() method gets invoked twice


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


class Base2:
    def __init__(self):
        print('Base.__init__')


class A1(Base2):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B1(Base2):
    def __init__(self):
        super().__init__()
        print('B.__init__')

# When you use this new version, you’ll find that each __init__() method only gets called once


class C1(A1, B1):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


if __name__ == '__main__':
    # c = C()
    c = C1()
    print('{0}'.format(C1.__mro__))
