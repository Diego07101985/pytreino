from itertools import groupby, tee

alunos = [
    {
        'nome': 'Luiz', 'nota': 'A'
    },
    {
        'nome': 'BOB', 'nota': 'B'
    },
    {
        'nome': 'John', 'nota': 'C'
    },
    {
        'nome': 'Lucas', 'nota': 'B'
    },
    {
        'nome': 'Edinaldo', 'nota': 'B'
    }
]


def ordena(item): return item['nota']


alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos  tiraram a nota {agrupamento}')
    print()
    # for aluno in valores_agrupados:
    #     print(f'Valores {aluno}')
