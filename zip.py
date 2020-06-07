from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo ', 'Rio de Janeiro', 'Belo horizonte', "Itaborai"]
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    estados,
    cidades)


for valor in cidades_estados:
    print(valor)
# print(list(cidades_estados))
