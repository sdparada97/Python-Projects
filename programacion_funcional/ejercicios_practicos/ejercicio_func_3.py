"""
Implementa una función recursiva que calcula el factorial de un número dado.
"""


def factorial_num(num: int) -> int:
    return 1 if num <= 1 else num * (factorial_num(num - 1))


if __name__ == "__main__":
    print(
        factorial_num(
            int(
                input("Escribe un numero para buscar el factorial: ")
                )
            )
        )
