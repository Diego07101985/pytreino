'''
Metaclasses saão classes que criam outras classes
'''


A = type('A', (), {'attr': 'Olá mundo'})
a = A()
print(a.attr)
print(a)
