# Mutaveis: Listas, Dicionarios
# Imutaveis: Tuplas, strings,números, True, False, None


def lista_de_clientes(cliente_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(cliente_iteravel)
    return lista


# lista_de_clientes_1 = ['Fabricio']
# clientes1 = lista_de_clientes(
#     ['João', 'Maria', 'Eduardo'], lista_de_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['Abraço'])

print(clientes2)
print(clientes3)
