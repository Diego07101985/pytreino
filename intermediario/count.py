from itertools import count
from types import GeneratorType
variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
# print(list(variavel))
print(next(variavel))
print(next(variavel))

print(isinstance(variavel, GeneratorType))

contador = count(start=0, step=-1)
list

for valor in contador:
    print(round(valor, 2))
    if valor >= 10 or valor <= -10:
        break
