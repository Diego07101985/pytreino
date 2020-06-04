def func1(func):
    return func()


def func2():
    return "func2"


def func3(func4, *args, **kwargs):
    return func4(*args, **kwargs)


def func4(*args, **kwargs):
    print(args)
    print(kwargs)
    return 'varios argumentos'


executandto = func3(func4, 1, 2, 3, 4, 5, abraco="free")

print(executandto)
