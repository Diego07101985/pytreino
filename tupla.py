t1 = (1, 2, 3, "mini")
t2 = 6, 7, 8, 9
t3 = t1 + t2

n1, n2, n3, *_ = t3
print(type(t1))
print(type(t2))

print(n1)
print(*_)

t1 = (1, 2, 'Luiz', 4) * 2

print(t1)
