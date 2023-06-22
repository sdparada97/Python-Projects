"""
Implementa una función que tome una lista de palabras y devuelva
una nueva lista que contenga sólo las palabras que tienen
más de 5 caracteres.
"""


def str_less_than_five_chars(word: str) -> bool:
    return len(word) > 5


if __name__ == "__main__":
    list_words = [
        input(f"Escriba una palabra para la lista pos({_}):")
        for _ in range(10)
    ]
    print()
    print(list_words)
    print(list(filter(str_less_than_five_chars, list_words)))
