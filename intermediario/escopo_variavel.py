variavel = "valor"


def func():
    print(variavel)


def func2():
    global variavel
    variavel = "outrovalor"
    print(variavel)


def func3(arg=None):
    return arg.replace('v', 'c')


func()
print(func3(arg=variavel))
func2()
print(variavel)
