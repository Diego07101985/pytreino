d1 = {'chave1': 'valor da chave'}

d1['outra chave'] = "Minha nova chave"


print(d1['outra chave'])


d2 = {

    "element": {
        'chave1': 123232,
        'chave2': 'vamos de dic',
        'chave3': "que lindo"
    },
    "element2": {
        'chave1': 123232,
        'chave2': 'vamos de dic',
        'chave3': "que lindo"
    }}


if 232 in d1:
    print(d1[232])


for k in d1:
    print(d1[k])

for k, v in d1.items():
    print(k)
    print(v)


for k, v in d2.items():
    print(f'\t{k}')
    for dados_k, dados_v in v.items():
        print(f'\t{dados_k} = {dados_v}')

d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ["testes"]}

print(d3)
d4 = d3.copy()

print(d4)

d4[1] = 'd'
print(d4)
print(d3)

print(d4.pop('d'))
d4.popitem()
print(d4)
