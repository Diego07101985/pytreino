class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # The __repr__() method returns the code representation of an instance, and is usually the text you would type to re-create the instance.

    def __repr__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)

    # if method not have a implementation of __str__(self): the method __repr__(self) will be call

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


if __name__ == "__main__":

    p = Pair(3, 4)  # call  function __repr__()
    p
    print(p)  # call  function __str__()
    #!r formatting code indicates that the output of __repr__() should be used instead of __str__(), the default
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))

    pass
