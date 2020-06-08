from dados import produtos, pessoas, lista


def filtra(produto):
    if produto['preco'] > 50:
        # warning
        # embora isso tenha no exemplo é bem zoado pq vc cria um parametro na entidade produto  que não existe modelo original
        # produto['e_caro'] = True
        return True


nova_lista = filter(filtra, produtos)
# nova_lista = [x for x in lista if x > 5]
for produto in nova_lista:
    print(produto)

print(list(nova_lista))
