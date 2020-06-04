
def movimento(test="1", msg="Hello World"):
    msg = msg.replace("o", "0")
    return f'{test} {msg}'
print(movimento())

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1/n2
divide = divisao(8, 0)

print(divide)

if divide:
    print(divide)
else:
    print("Conta inválida")


def f(var):
    print(var)

def dumb():
    return f
var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('Blaaaaaa')
