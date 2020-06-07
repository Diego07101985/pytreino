string = '0123456789012345678901234567890123456789012345678901234567890123456789'


lista_string = string.split()
n = 10


contadores = [i for i in range(0, len(string), n)]
print(contadores)
tuplas = [(i, i+n) for i in range(0, len(string), n)]
print(tuplas)
lista = [string[i:i+n] for i in range(0, len(string), n)]

retorno = '.'.join(lista)
print(lista)
print(retorno)
