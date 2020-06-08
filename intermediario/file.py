# file = open('text.txt', 'w+')

# file.write("Linha 1 \n")
# file.write("Linha 2 \n")
# file.write("Linha 3 \n")


# file.seek(0, 0)
# print('Lendo Linhas')
# print(file.readline(), end='')
# print(file.readline())
# file.seek(0, 0)

# for linha in file.readlines():
#     print(linha, end='')

# file.close()

# with open('text.txt', 'w+') as file:
#     file.write('Linha 1')
#     file.write('Linha 2')
#     file.write('Linha 3')
#     file.seek(0)
#     print(file.read())

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 23
    },
    'Pessoa 2': {
        'nome': 'Maria',
        'idade': 26
    },
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('test.json', 'w+') as file:
    file.write(d1_json)


with open('test.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)
    print(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
