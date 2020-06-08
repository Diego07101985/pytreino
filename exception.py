
try:
    a = []
    print(a[1])
except NameError as err:
    print(err)
except (IndexError, KeyError) as err:
    print(err)
except Exception as err:
    print("Ocorreu erro inesperado")
else:
    print("Foi executado com sucesso ")
finally:
    a = [1, 2]
    print(a[1])
    print('Finalmente')
