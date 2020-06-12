'''
PILHA (stack) = LIFO -last in, first out
Fila (queue) = FIFO - Fist in , first out
'''

from collections import deque
from time import sleep

# fila = deque(maxlen=5)
# print(deque)

# fila.append('Paulo')
# fila.append('Julio')
# fila.append('Loide')
# fila.append('Paola')

# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')

# for nome in fila:
#     print(nome)


fila = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)

# fila .insert(2, 'Abraco')

print(fila.index(3))
print(fila)


# fila = deque(maxlen=10)

# for i in range(1000):
#     fila.append(i)
#     sleep(1)
#     print(fila)
