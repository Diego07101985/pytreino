"""
1 - Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5
3 - Saber se o numero é multiplo de 5:
4 - Saber se é multiplo de 3
5 - Saber se naão é multiplo de 3 e 5 
    passa fome 
"""


def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    elif n % 3 == 0:
        return 'Bacon'
    elif n % 5 == 0:
        return 'Ovos'
    else:
        return 'Passar fome'
