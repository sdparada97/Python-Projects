"""
Implementa una función que genere una secuencia de números
Fibonacci utilizando recursión.
"""


def fibonacci(num: int) -> None:
    return num if num in {0, 1} else fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    num_range = int(input("Escribe la cantidad de veces para fibonacci: "))
    print([fibonacci(num) for num in range(num_range)])
