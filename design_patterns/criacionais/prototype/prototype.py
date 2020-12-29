"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
#import for correction anotations future in order creation 
from __future__ import annotations

from typing import List
from copy import deepcopy

name1 = 'Luiz'
name2 = name1 

name1 = 'Outra Coisa'
print(name1)
print(name2)

class StringReprMixin:
    def __str__(self):
        params = ','.join([f'{k}={v}' for k,v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()

class Tv(StringReprMixin):
    def __init__(self,name: str,polegadas: int)->None:
        self.name = name
        self.polegadas = polegadas
        self.especifications: List[Specification] = []

    def add_especifications(self,specification:Specification)-> None:
        self.especifications.append(specification)

    def clone(self) -> Tv:
        return deepcopy(self)

class Specification(StringReprMixin):
    def __init__(self,modelo,resolucao):
        self.modelo = modelo
        self.resolucao = resolucao

if __name__ == "__main__":
    tv_samsung = Tv('Tv Qled',60)
    specification_tu7000 = Specification('TU8000','4k')
    tv_samsung.add_especifications(specification_tu7000)

    tv_samsung_55 = tv_samsung.clone()
    tv_samsung_55.polegadas = 55

    print(tv_samsung)
    print(tv_samsung_55)


