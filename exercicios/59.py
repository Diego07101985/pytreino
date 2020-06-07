
lista = [
    [1, 3, 44, 5, 6, 7, 1, 2, 3, 4],
    [1, 3, 4, 5, 46, 7, 1, 2, 63, 4],
    [1, 3, 4, 53, 6, 7, 1, 2, 3, 4],
    [1, 3, 4, 5, 6, 7, 1, 2, 3, 4],
    [1, 32, 4, 5, 6, 7, 1, 2, 3, 4],
    [1, 3, 4, 5, 6, 7, 1, 2, 3, 4],
    [1, 3, 4, 5, 6, 27, 1, 2, 3, 84],
    [1, 3, 4, 5, 6, 7, 1, 2, 3, 4],
    [1, 3, 4, 35, 6, 7, 1, 2, 3, 4],
    [1, 3, 4, 5, 6, 57, 1, 2, 63, 4]]


def find_elements_duplicate(lista):
    new_lista = []
    for inner_lista in lista:
        duplicate_number = 0
        lista_duplicate = []
        for element_inner in inner_lista:
            if element_inner in inner_lista:
                lista_duplicate.append(element_inner)
                duplicate_number = duplicate_number + 1
            if duplicate_number > 2:
                break
            new_lista.append(lista_duplicate)
    return new_lista


print(find_elements_duplicate(lista))
