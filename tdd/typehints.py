from typing import List, Union, Tuple, Dict, NewType, Callable

# Primitivos
numero: int = 10
flutuante: float = 12.2
booleano: bool = True
string: str = "aloalo"


# Sequencias

lista: List[int] = [1, 24, 12]

lista_str_int: List[Union[int, str]] = [1, 2, 3, 'as']
tupla: Tuple[int, int, int] = (1, 2, 3)


# Dicionarios e conjuntos

pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Luiz Otávio', 'sobrenome': 'miranda', 'idade': 30}

# Outro Tipo
UserId = NewType('UserId', int)
user_id = UserId(233232)


# def retorna_funcao(funcao: Callable[[], None]) -> Callable:
#     return funcao


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return x + y


retorna_funcao(soma)(10, 20)
