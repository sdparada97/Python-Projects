"""
Implementa una función que tome una lista de números y devuelva una nueva lista
donde cada elemento sea el doble del valor original.
"""


def double_value(num: int) -> int:
    return num * 2


if __name__ == "__main__":
    list_num = [
        int(input(f"Escriba un numero para la lista pos({_}):"))
        for _ in range(10)
    ]
    print()
    print(list_num)
    print(list(map(double_value, list_num)))
