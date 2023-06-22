"""
Implementa una función que tome una lista de números y devuelva
True si todos los elementos son mayores que 0,
y False en caso contrario.
"""
from typing import List


def validator_is_greater_than_zero(list_num: List[int]) -> bool:
    return not list(filter(lambda val: val < 0, list_num))


if __name__ == "__main__":
    list_num = [
        int(input(f"Escriba un numero para la lista pos({_}):"))
        for _ in range(10)
    ]

    print(validator_is_greater_than_zero(list_num))
